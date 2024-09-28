from flask import Flask, request, jsonify
import jwt
import os
from cryptography.fernet import Fernet
from datetime import datetime, timedelta
from jwt import ExpiredSignatureError, InvalidTokenError  # Import necessary exceptions

app = Flask(__name__)

# Symmetric key for JWT encryption (set from environment variable)
symmetric_key = os.getenv('SYMMETRIC_KEY')

if not symmetric_key:
    raise ValueError("SYMMETRIC_KEY environment variable is not set.")

# Ensure the symmetric key is a valid Fernet key
try:
    fernet = Fernet(symmetric_key)
except Exception as e:
    raise ValueError("Invalid SYMMETRIC_KEY. It must be a valid Fernet key.") from e

# Encrypt a JWT using Fernet encryption
def encrypt_token(token):
    encrypted_token = fernet.encrypt(token.encode())
    return encrypted_token

# Decrypt an encrypted JWT
def decrypt_token(encrypted_token):
    decrypted_token = fernet.decrypt(encrypted_token.encode()).decode()
    return decrypted_token

# Issue JWT token endpoint
@app.route('/issue_token', methods=['POST'])
def issue_token():
    data = request.get_json()
    email = data.get('email')

    if not email:
        return jsonify({"error": "Email is required"}), 400

    # Define payload with email and expiration
    payload = {
        'email': email,
        'exp': datetime.utcnow() + timedelta(minutes=1)  # Token expires in
    }

    # Generate JWT token
    token = jwt.encode(payload, symmetric_key, algorithm='HS256')

    # Encrypt the token using the symmetric key
    encrypted_token = encrypt_token(token)

    return jsonify({"token": encrypted_token.decode('utf-8')}), 200

@app.route('/verify_token', methods=['POST'])
def verify_token():
    data = request.get_json()
    encrypted_token = data.get('token')

    if not encrypted_token:
        return jsonify({"error": "Token is required"}), 400

    try:
        # Decrypt the token
        token = decrypt_token(encrypted_token)

        # Decode the token
        decoded_token = jwt.decode(token, symmetric_key, algorithms=['HS256'])

        # Get the expiration time from the decoded token
        exp = datetime.utcfromtimestamp(decoded_token['exp'])
        now = datetime.utcnow()

        # Check how much time is remaining
        time_remaining = (exp - now).total_seconds()

        if time_remaining < 15:
            # Refresh the token if it's about to expire (less than 15 seconds)
            new_payload = {
                'email': decoded_token['email'],
                'exp': datetime.utcnow() + timedelta(seconds=30)  # Refresh the token for 30 more seconds
            }
            new_token = jwt.encode(new_payload, symmetric_key, algorithm='HS256')
            encrypted_new_token = encrypt_token(new_token)
            return jsonify({
                "message": "Token was refreshed",
                "token": encrypted_new_token.decode('utf-8')
            }), 200

        # If the token is still valid and not near expiration
        return jsonify({
            "message": "Token is valid",
            "token": encrypted_token,  # Return the same encrypted token without decoding
            "time_remaining": time_remaining
        }), 200

    except ExpiredSignatureError:
        return jsonify({"error": "Token has expired"}), 401
    except InvalidTokenError:
        return jsonify({"error": "Invalid token"}), 401
    except Exception as e:
        # Handle other potential exceptions
        return jsonify({"error": "An error occurred during token verification", "details": str(e)}), 500

if __name__ == '__main__':
    # Ensure SSL certificates exist or adjust as needed
    ssl_cert = '/etc/ssl/certs/csp.crt'
    ssl_key = '/etc/ssl/certs/csp.key'

    if not os.path.exists(ssl_cert) or not os.path.exists(ssl_key):
        raise FileNotFoundError("SSL certificate or key not found.")

    app.run(host='0.0.0.0', port=443, ssl_context=(ssl_cert, ssl_key))
