from flask import Flask
from flask_cors import CORS
from urls import webapp

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})


app.register_blueprint(webapp)


@webapp.route('/')
def index():
    return "Welcome to the Weather App!"


if __name__ == '__main__':
    app.run(debug=True)
