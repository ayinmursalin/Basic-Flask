from app import create_app
from flask import request, jsonify
from datetime import timedelta
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_jwt_extended import get_jwt_identity, get_jwt
from flask_jwt_extended import jwt_required, verify_jwt_in_request
from functools import wraps

app = create_app()


# Create custom decorator to check user in admin only
def admin_required():
    def wrapper(func):
        @wraps(func)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()

            if claims["is_admin"]:
                return func()

            return jsonify({"message": "Admin only"}), 403

        return decorator

    return wrapper


@app.route("/")
def index():
    return "Hello World!"


@app.route("/api/auth/login", methods=["POST"])
def login():
    data = request.get_json()

    if data["username"] and data["password"] == "asdf1234":
        access_token = create_access_token(
            data["username"],
            expires_delta=timedelta(days=7),
            additional_claims={"is_admin": data["username"] == "admin"},
        )  # Store user id instead of username as JWT identity
        refresh_token = create_refresh_token(data["username"])

        return jsonify(
            {
                "message": "Login Success",
                "tokens": {"access": access_token, "refresh": refresh_token},
            }
        )

    return jsonify({"message": "Login Failed"}), 401


@app.route("/api/auth/profile")
@jwt_required()
@admin_required()
def get_profile():
    user = get_jwt_identity()

    return jsonify({"message": "Get profile success", "data": user})


if __name__ == "__main__":
    app.run(debug=True)
