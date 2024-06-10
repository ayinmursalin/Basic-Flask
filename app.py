from flask import Flask, jsonify
from flask_jwt_extended import JWTManager


jwt = JWTManager()


# Custom unauthorized callback
@jwt.unauthorized_loader
def custom_unauthorized_response(msg):
    return jsonify({"message": "Unauthorized"}), 401


def create_app():
    app = Flask(__name__)
    app.config["JWT_SECRET_KEY"] = "20468551-e9dc-442e-a66f-eec221f3d646"

    jwt.init_app(app)

    return app
