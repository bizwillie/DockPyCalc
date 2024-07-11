import psycopg2
from psycopg2 import sql

# Database connection parameters
DATABASE = {
    'dbname': 'auth_db',
    'user': 'auth_user',
    'password': 'password',
    'host': 'auth_db',
    'port': '5432'
}

# Create connection to the database
conn = psycopg2.connect(**DATABASE)
conn.autocommit = True

# Create a cursor object using the connection
cur = conn.cursor()

# SQL command to create the users table
create_table_command = """
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL
);
"""

# Execute the command
cur.execute(create_table_command)

# Close the cursor and connection
cur.close()
conn.close()
