import requests

# Define the URLs for the services
RA_URL = "https://localhost:5443/login"  # RA login endpoint

# Disable SSL warnings (for local testing with self-signed certs)
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

# Simulate user login request
def login(username, password):
    # Login data to send to RA
    login_data = {
        "username": username,
        "password": password
    }
    
    try:
        # Send POST request to RA for login
        response = requests.post(RA_URL, json=login_data, verify=False)  # Change 'verify=False' if using self-signed certs
        if response.status_code == 200:
            print("Login successful!")
            token = response.json().get('token')
            print(f"Received token: {token}")
            return token
        elif response.status_code == 403:
            print("Invalid credentials. Login failed.")
            print(f"Res: {response.status_code} - {response.text}")
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while logging in: {e}")

if __name__ == "__main__":
    # Simulate login credentials
    username = "alice"
    password = "supersecretpassword"
    
    # User logs in and receives a token
    token = login(username, password)
    
    # The token can now be used for subsequent requests
    if token:
        print("Use this token for future authenticated requests.")
