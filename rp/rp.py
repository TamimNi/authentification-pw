from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)

# Define the CSP verification URL
VERIFY_URL = "https://verifier_service:443/verify_token"
CORS(app, resources={r"/*": {"origins": "*"}})

# Route to verify the token by forwarding the request to the CSP service
@app.route('/secret', methods=['POST'])
def share_secret():
    verification = verify_token()
    
    # Check if verification is a response object
    if isinstance(verification, requests.Response):
        if verification.status_code == 200:
            response = verification.json()
            response['secret'] = "Hash and salt your passwords!"
            return jsonify(response), verification.status_code
        else:
            return jsonify({"error": "Token not valid"}), 403
    else:
        # If verification is not a response, it's an error message
        return verification  # This will return the error message

def verify_token():
    # Get the token from the request
    data = request.json
    token = data.get('token')

    if not token:
        return jsonify({"error": "Token is required"}), 400

    try:
        verifier_response = requests.post(VERIFY_URL, json={"token": token}, verify=False)
        return verifier_response  # Return the response object directly
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500  # Return an error message and status code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443, ssl_context=('/etc/ssl/certs/rp.crt', '/etc/ssl/certs/rp.key'))
