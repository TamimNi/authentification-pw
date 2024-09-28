from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Define the CSP verification URL
CSP_VERIFY_URL = "https://csp_service:443/verify_token"

# Route to verify the token by forwarding the request to the CSP service
@app.route('/verify_token', methods=['POST'])
def verify_token():
    # Get the token from the request
    data = request.json
    token = data.get('token')

    if not token:
        return jsonify({"error": "Token is required"}), 400

    try:
        # Forward the token to the CSP service for verification
        csp_response = requests.post(CSP_VERIFY_URL, json={"token": token}, verify=False)

        # Return the CSP service response to the client
        return jsonify(csp_response.json()), csp_response.status_code

    except requests.exceptions.RequestException as e:
        # Handle errors from the CSP service request
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443, ssl_context=('/etc/ssl/certs/verifier.crt', '/etc/ssl/certs/verifier.key'))
