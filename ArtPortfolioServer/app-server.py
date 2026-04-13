from flask import Flask, request, jsonify
from flask_cors import CORS
# Create an instance of the Flask class
app = Flask(__name__)
# This will enable CORS for all routes from any origin
CORS(app)

# Use the route() decorator to tell Flask what URL and HTTP method (GET, POST) should trigger the function
@app.route("/test", methods=['GET'])
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/add', methods=['GET'])
def add_numbers():
    x = float(request.args.get('x', 0))
    y = float(request.args.get('y', 0))
        
    result = x+ y
        
    # Return the result as a JSON response
    return jsonify({'sum': result})

@app.route('/register', methods=['GET'])
def register_user()
    return "<p>Not, Implemented!</p>"

@app.route('/login', methods=['GET'])
def login_user()
    return "<p>Not, Implemented!</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9001, debug=True)