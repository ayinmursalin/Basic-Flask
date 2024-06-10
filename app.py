from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "insert-secret-key"  # Change secret key

    # Insert Configuration

    return app
