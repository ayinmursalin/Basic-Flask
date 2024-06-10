from app import create_app
from flask import request, jsonify
from datetime import timedelta
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

app = create_app()


@app.route("/")
def index():
    return "Hello World!"


@app.route("/api/auth/login", methods=["POST"])
def login():
    data = request.get_json()
    if data["username"] == "admin" and data["password"] == "admin":
        access_token = create_access_token(
            data["username"],
            expires_delta=timedelta(seconds=60),
        )  # Store user id instead of username as JWT identity
        refresh_token = create_refresh_token(data["username"])

        return jsonify(
            {
                "message": "Login Success",
                "tokens": {"access": access_token, "refresh": refresh_token},
            }
        )

    return ""


@app.route("/api/auth/profile")
@jwt_required()
def get_profile():
    user = get_jwt_identity()

    return jsonify({"message": "Get profile success", "data": user})


if __name__ == "__main__":
    app.run(debug=True)
