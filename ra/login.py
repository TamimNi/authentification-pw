# models.py
import secrets
from werkzeug.security import generate_password_hash, check_password_hash
from db import get_db_connection

def login_user(email, password):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT password, salt FROM public.users WHERE email = %s", (email,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if user:
        stored_password, salt = user
        if check_password_hash(stored_password, password + salt):
            return True  # Login successful
        else:
            return False  # Invalid credentials
    else:
        return False  # Invalid credentials
