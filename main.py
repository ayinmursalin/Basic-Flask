from flask import jsonify, request, render_template
from app import create_app
from app import db
from models import *

app = create_app()


@app.route("/")
def index():
    return render_template('index.html', my_value=2, my_list=["Hehe", "huhu", "hoho"])


@app.route("/api/users", methods=["GET", "POST"])
def users():
    if request.method == "POST":
        # Create new User
        data = request.get_json()
        user = User(
            email=data["email"],
            name=data["name"],
            password=data["password"],
        )

        db.session.add(user)
        db.session.commit()

        return jsonify({"message": "Successfully create new User", "data": user})

    users = User.query.all()
    return jsonify({"message": "Successfully get all User", "data": users})


if __name__ == "__main__":
    app.run(debug=True)
