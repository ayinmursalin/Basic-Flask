from flask import Blueprint, request, jsonify
from utils import bcrypt

auth = Blueprint("auth", __name__, url_prefix="/api")


@auth.route("/create-password", methods=["POST"])
def create_password():
    data = request.get_json()

    return jsonify(
        {
            "message": "Create Hashed Password Success",
            "data": {
                "password": data["password"],
                "hashed_password": bcrypt.generate_password_hash(
                    data["password"]
                ).decode("utf-8"),
            },
        }
    )


@auth.route("/check-password", methods=["POST"])
def check_password():
    data = request.get_json()

    return jsonify(
        {
            "message": "Check Hashed Password",
            "data": {
                "is_valid": bcrypt.check_password_hash(
                    data["hashed_password"], data["password"]
                )
            },
        }
    )
