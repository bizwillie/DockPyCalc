# auth.py - Enhanced Authentication and session management module

from datetime import datetime, timedelta
from passlib.context import CryptContext
import psycopg2

# Database connection
conn = psycopg2.connect(
    dbname='auth_db',
    user='auth_user',
    password='password',
    host='auth_db'
)
cursor = conn.cursor()

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Helper functions
def hash_password(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def password_policy(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    if not any(char.isdigit() for char in password):
        return False, "Password must contain at least one digit"
    if not any(char.isupper() for char in password):
        return False, "Password must contain at least one uppercase letter"
    if not any(char.islower() for char in password):
        return False, "Password must contain at least one lowercase letter"
    if not any(char in "!@#$%^&*()_+-=[]{}|;:'\",.<>?/~`" for char in password):
        return False, "Password must contain at least one special character"
    return True, ""

def authenticate(username, password):
    cursor.execute("SELECT password, last_password_change FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()
    if result:
        stored_password, last_password_change = result
        if verify_password(password, stored_password):
            # Check if password is expired
            if datetime.now() - last_password_change > timedelta(days=90):
                return False, "Password expired, please change your password"
            return True, ""
    return False, "Invalid username or password"

def change_password(username, old_password, new_password):
    auth, msg = authenticate(username, old_password)
    if auth:
        valid, policy_msg = password_policy(new_password)
        if valid:
            hashed_new_password = hash_password(new_password)
            cursor.execute(
                "UPDATE users SET password = %s, last_password_change = %s WHERE username = %s",
                (hashed_new_password, datetime.now(), username)
            )
            conn.commit()
            return True, "Password changed successfully"
        else:
            return False, policy_msg
    else:
        return False, msg

def create_user(username, password):
    valid, policy_msg = password_policy(password)
    if valid:
        hashed_password = hash_password(password)
        cursor.execute(
            "INSERT INTO users (username, password, last_password_change) VALUES (%s, %s, %s)",
            (username, hashed_password, datetime.now())
        )
        conn.commit()
        return True, "User created successfully"
    else:
        return False, policy_msg

def delete_user(username):
    cursor.execute("DELETE FROM users WHERE username = %s", (username,))
    conn.commit()
    return True, "User deleted successfully"
