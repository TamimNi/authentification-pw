# routes.py
from flask import Flask, request, jsonify
from login import login_user
from register import register_user

def create_routes(app: Flask):
    @app.route('/register', methods=['POST'])
    def register_new_user():
        data = request.json
        email = data.get('email')
        password = data.get('password')

        if register_user(email, password):
            return jsonify({"message": "User registered successfully"}), 201
        else:
            return jsonify({"message": "User already exists"}), 409

    @app.route('/login', methods=['POST'])
    def login_user_route():
        data = request.json
        email = data.get('email')
        password = data.get('password')
        token = login_user(email, password)
        if token:
            return jsonify({"message": "Login successful", "token": token}), 200
        else:
            return jsonify({"message": "Invalid credentials"}), 403
