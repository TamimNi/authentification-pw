# ra_service.py (Registration Authority) - Running on HTTPS port 5443
from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

CSP_URL = "https://csp_service:443/issue_token"  # HTTPS endpoint for CSP

@app.route('/login', methods=['POST'])
def login_user():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Simulate identity proofing with Postgres or external DB (this can be extended)
    # Here, we'll just mock it
    if username == 'alice' and password == 'supersecretpassword':
       
        return jsonify({"message": "Login successful"}), 200
        # Forward the request to CSP to issue a token
        '''
        csp_response = requests.post(
            CSP_URL,
            json={"username": username},
            verify='/etc/ssl/certs/csp.crt'  # Verify CSP's certificate
        )
        
        if csp_response.status_code == 200:
            token = csp_response.json()['token']
 
            return jsonify({"message": "Login successful", "token": token}), 200
        return jsonify({"message": "Token issuance failed"}), 500
        '''
        return jsonify({"message": "Invalid credentials"}), 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443, ssl_context=('/etc/ssl/certs/ra.crt', '/etc/ssl/certs/ra.key'))
