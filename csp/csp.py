from flask import Flask, request, jsonify
import jwt
import os
from cryptography.fernet import Fernet
from datetime import datetime, timedelta

app = Flask(__name__)

# Symmetric key for JWT encryption (set from environment variable)
symmetric_key = os.getenv('SYMMETRIC_KEY')

# Encrypt a JWT using Fernet encryption
def encrypt_token(token):
    fernet = Fernet(symmetric_key)
    encrypted_token = fernet.encrypt(token.encode())
    return encrypted_token

# Decrypt an encrypted JWT
def decrypt_token(encrypted_token):
    fernet = Fernet(symmetric_key)
    decrypted_token = fernet.decrypt(encrypted_token).decode()
    return decrypted_token

# Issue JWT token endpoint
@app.route('/issue_token', methods=['POST'])
def issue_token():
    data = request.json
    email = data.get('email')

    if not email:
        return jsonify({"error": "Email is required"}), 400

    # Define payload with email and expiration
    payload = {
        'email': email,
        'exp': datetime.utcnow() + timedelta(minutes=1)  # Token expires in 30 minutes
    }

    # Generate JWT token
    token = jwt.encode(payload, symmetric_key, algorithm='HS256')

    # Encrypt the token using the symmetric key
    encrypted_token = encrypt_token(token)

    return jsonify({"token": encrypted_token.decode('utf-8')}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443, ssl_context=('/etc/ssl/certs/csp.crt', '/etc/ssl/certs/csp.key'))
