from flask import Flask, jsonify, request

app = Flask(__name__)

# Initial memory-based storage for users
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

@app.route('/')
def home():
    """Root endpoint returning a welcome message."""
    return "Welcome to the Flask API!"

@app.route('/data')
def get_data():
    """Returns a list of all usernames stored in the API."""
    return jsonify(list(users.keys()))

@app.route('/status')
def get_status():
    """Returns the status of the API."""
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    """Returns the full object for a given username or a 404 error."""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """Adds a new user to the users dictionary based on POSTed JSON data."""
    # Check if the request contains valid JSON
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    # Validate that 'username' is present in the data
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Check if user already exists
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Add user to the dictionary
    users[username] = data
    
    # Return confirmation message and the added user data
    response = {
        "message": "User added",
        "user": data
    }
    return jsonify(response), 201

if __name__ == "__main__":
    app.run()
