#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_jwt_extended import create_refresh_token
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

app = Flask(__name__)
auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "user2": {"username": "user2", "password": generate_password_hash("password"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username),password):
        return username

@app.route('/basic-protected',  methods=['GET'])
@auth.login_required
def index():
        return "Basic Auth: Access Granted"

@app.route('/login', methods =['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "user1" or password != "password":
        return jsonify({"msg": "Bad username or password"}), 401
    else:
        access_token = create_access_token(identity="user1", fresh=True)
        refresh_token = create_refresh_token(identity="user1")
        return jsonify(access_token=access_token, refresh_token=refresh_token)