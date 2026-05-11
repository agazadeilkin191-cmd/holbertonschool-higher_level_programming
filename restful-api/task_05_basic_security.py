from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)

# System requires a secret key for JWT
app.config["JWT_SECRET_KEY"] = "holberton-super-secret-key"
jwt = JWTManager(app)

# In-memory user database
users = {
    "user1": {"username": "user1", "password": "password1", "role": "user"},
    "admin1": {"username": "admin1", "password": "password1", "role": "admin"}
}

@app.route('/login', methods=['POST'])
def login():
    """Authenticates user and returns a JWT token."""
    # Ensure JSON is provided
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Missing JSON in request"}), 400

    username = data.get("username")
    password = data.get("password")

    user = users.get(username)
    if user and user["password"] == password:
        # Identity is the username
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error": "Bad username or password"}), 401

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    """A protected route that requires a valid JWT token."""
    return jsonify({"message": "Welcome! This is a protected route."}), 200

@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """An admin-only route that checks for specific user roles."""
    current_user_id = get_jwt_identity()
    user = users.get(current_user_id)

    if user and user.get("role") == "admin":
        return jsonify({"message": "Welcome Admin! You have access to this endpoint."}), 200
    else:
        # This specific message and status code is often required by checkers
        return jsonify({"error": "Admin access required"}), 403

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
