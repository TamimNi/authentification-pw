# models.py
import secrets
from werkzeug.security import generate_password_hash, check_password_hash
from db import get_db_connection

def register_user(email, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM public.users WHERE email = %s", (email,))
    existing_user = cursor.fetchone()
    
    if existing_user:
        cursor.close()
        conn.close()
        return None  # User already exists

    # Generate a salt and hash the password with it
    salt = secrets.token_hex(16)
    hashed_password = generate_password_hash(password + salt, method='pbkdf2:sha256')

    # Insert the new user into the database
    cursor.execute("INSERT INTO public.users (email, password, salt) VALUES (%s, %s, %s)", (email, hashed_password, salt))
    conn.commit()

    cursor.close()
    conn.close()
    return True  # User registered successfully
