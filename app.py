from flask import Flask
from flask_jwt_extended import JWTManager


jwt = JWTManager()


def create_app():
    app = Flask(__name__)
    app.config["JWT_SECRET_KEY"] = "20468551-e9dc-442e-a66f-eec221f3d646"

    jwt.init_app(app)

    return app
