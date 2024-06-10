from flask import Flask
from utils import bcrypt
from routes.auth import auth as auth_blueprint


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "insert-secret-key"  # Change secret key

    # Insert Configuration
    bcrypt.init_app(app)

    # Register Blueprint
    app.register_blueprint(auth_blueprint)

    return app
