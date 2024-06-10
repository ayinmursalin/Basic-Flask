from flask import Flask
from routes.auth import auth
from routes.post import post

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "insert-secret-key"  # Change secret key

    # Insert Configuration
    app.register_blueprint(auth)
    app.register_blueprint(post)

    return app
