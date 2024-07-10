# auth.py - Authentication and session management module

users = {
    'user': 'pass'
}

def authenticate(username, password):
    return username in users and users[username] == password
