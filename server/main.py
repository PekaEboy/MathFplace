import flask

app = flask.Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/login', methods=['POST'])
def api_login():
    return flask.jsonify({
        "login": "AlphaAccount",
        "password": "123456"
    })

@app.route('/api/register', methods=['POST'])
def api_register():
      return flask.jsonify({
           "login": "AlphaAccount",
           "password": "123456"
      })

if __name__ == '__main__':
    app.run()