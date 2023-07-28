from flask import Flask, jsonify
from flask_cors import CORS

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

# sanity check route
@app.route('/api/login', methods=['GET'])
def login():
    return jsonify({
        "login": "Account",
        "password": "12345"
        })

@app.route('/api/signup', methods=['POST'])
def signup():
    return jsonify()
if __name__ == '__main__':
    app.run()