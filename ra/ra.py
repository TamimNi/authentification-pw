# ra_service.py (Registration Authority) - Running on HTTPS port 5443
from flask import Flask
import psycopg2
import os
import secrets
from werkzeug.security import generate_password_hash, check_password_hash  
from my_routes import create_routes

app = Flask(__name__)
create_routes(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443, ssl_context=('/etc/ssl/certs/ra.crt', '/etc/ssl/certs/ra.key'))

