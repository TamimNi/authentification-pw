from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Define the CSP verification URL
VERIFY_URL = "https://verifier_service:443/verify_token"

# Route to verify the token by forwarding the request to the CSP service
@app.route('/secret', methods=['POST'])
def share_secret():
    verification = verify_token()
    
    if verification.status_code == 200:
        response = verification.json()
        response['secret'] = "Hash and salt your passwords!"
        return jsonify(response), verification.status_code
    else:
        return jsonify({"error": "Token not valid"}), 403

    
def verify_token():
    # Get the token from the request
    data = request.json
    token = data.get('token')

    if not token:
        return jsonify({"error": "Token is required"}), 400

    try:
        verifier_response = requests.post(VERIFY_URL, json={"token": token}, verify=False)
        return verifier_response
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443, ssl_context=('/etc/ssl/certs/rp.crt', '/etc/ssl/certs/rp.key'))
