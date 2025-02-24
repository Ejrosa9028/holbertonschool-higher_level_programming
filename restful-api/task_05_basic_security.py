#!/usr/bin/python3
'''
API segura con Flask utilizando autenticación básica y JWT.

Este servidor maneja diferentes tipos de autenticación:
- Autenticación básica para proteger rutas con usuario y contraseña.
- Autenticación con JSON Web Token (JWT) para acceso seguro a rutas.
- Control de acceso basado en roles para restringir ciertas rutas.

Autor: Tu Nombre
'''

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

# Inicialización de Flask y módulos de autenticación
app = Flask(__name__)
auth = HTTPBasicAuth()
app.config['JWT_SECRET_KEY'] = 'clave_secreta_segura'
jwt = JWTManager(app)

# Base de datos de usuarios (almacenada en memoria)
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

# Autenticación básica
@auth.verify_password
def verify_password(username, password):
    '''Verifica si el usuario y contraseña son correctos.''' 
    if username in users and check_password_hash(users[username]['password'], password):
        return username
    return None

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    '''Ruta protegida con autenticación básica.''' 
    return jsonify({"message": "Basic Auth: Access Granted"})

# Autenticación con JWT
@app.route('/login', methods=['POST'])
def login():
    '''Autenticación JWT: Genera un token si las credenciales son válidas.''' 
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if username in users and check_password_hash(users[username]['password'], password):
        access_token = create_access_token(identity={"username": username, "role": users[username]['role']})
        return jsonify(access_token=access_token)
    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    '''Ruta protegida con JWT.''' 
    return jsonify({"message": "JWT Auth: Access Granted"})

@app.route('/admin-only')
@jwt_required()
def admin_only():
    '''Ruta protegida solo para administradores.''' 
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return jsonify({"message": "Admin Access: Granted"})

if __name__ == '__main__':
    app.run(debug=True)
