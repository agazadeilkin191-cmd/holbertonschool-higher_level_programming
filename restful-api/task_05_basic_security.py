from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

app = Flask(__name__)

# Təhlükəsizlik üçün gizli açar (Secret Key)
app.config['JWT_SECRET_KEY'] = 'your_super_secret_key'  
jwt = JWTManager(app)
auth = HTTPBasicAuth()

# İstifadəçi məlumatları (Şərtə uyğun olaraq lüğət strukturunda)
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# --- Basic Authentication Tənzimləmələri ---

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]['password'], password):
        return username
    return None

# --- JWT Xəta İşləyiciləri (Custom Error Handlers) ---
# Tapşırıqda xüsusi olaraq bütün xətaların 401 qaytarması tələb olunur

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401


# --- Marşrutlar (Endpoints) ---

# 1. Basic Auth ilə qorunan marşrut
@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

# 2. Login marşrutu (JWT token almaq üçün)
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({"error": "Missing username or password"}), 400

    username = data.get('username')
    password = data.get('password')

    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        # Rol məlumatını tokenin içinə yerləşdiririk (identity olaraq lüğət göndəririk)
        access_token = create_access_token(identity={'username': username, 'role': user['role']})
        return jsonify(access_token=access_token)
    
    return jsonify({"error": "Bad username or password"}), 401

# 3. JWT ilə qorunan marşrut
@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

# 4. Rol əsaslı qorunan marşrut (Yalnız Adminlər üçün)
@app.route('/admin-only')
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if current_user.get('role') != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    
    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
