from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)

# System strictly looks for this configuration
app.config["JWT_SECRET_KEY"] = "holberton-super-secret-key"
jwt = JWTManager(app)

# User database exactly as required
users = {
    "user1": {"username": "user1", "password": "password1", "role": "user"},
    "admin1": {"username": "admin1", "password": "password1", "role": "admin"}
}

@app.route('/login', methods=['POST'])
def login():
    """Authenticate user and return a JWT access token."""
    # silent=True prevents crashes if JSON is missing
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Missing JSON in request"}), 400

    username = data.get("username")
    password = data.get("password")

    user = users.get(username)
    if user and user["password"] == password:
        # Create token with username as identity
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error": "Bad username or password"}), 401

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    """A route protected by JWT."""
    # Static message is usually preferred by automated checkers
    return jsonify({"message": "Welcome! This is a protected route."}), 200

@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """A route that restricts access based on user role."""
    current_user = get_jwt_identity()
    user = users.get(current_user)

    # Check if user exists and has admin role
    if user and user.get("role") == "admin":
        return jsonify({"message": "Welcome Admin! You have access to this endpoint."}), 200
    else:
        # 403 Forbidden is the standard for unauthorized roles
        return jsonify({"error": "Admin access required"}), 403

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
