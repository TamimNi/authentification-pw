# models.py
import secrets
import requests
from werkzeug.security import generate_password_hash, check_password_hash
from db import get_db_connection

CSP_URL = "https://csp_service:443/issue_token"  # HTTPS endpoint for CSP
cert_path = '/etc/ssl/certs/csp.crt'
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
            return request_jwt(email)    
        else:
            return False  # Invalid credentials
    else:
        return False  # Invalid credentials

def request_jwt(email):
    payload = {"email": email}
    try:
        response = requests.post(CSP_URL, json=payload, verify=False)        
        if response.status_code == 200:
            return response.json().get('token')
    except Exception as e:
            return f"Exception occurred: {e}"
    return