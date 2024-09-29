from flask import Flask
from flask_cors import CORS  # Import flask-cors
from my_routes import create_routes

app = Flask(__name__)

# Enable CORS for all routes and origins
CORS(app, resources={r"/*": {"origins": "*"}})

create_routes(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443, ssl_context=('/etc/ssl/certs/ra.crt', '/etc/ssl/certs/ra.key'))
