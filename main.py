from flask import jsonify
from app import create_app

app = create_app()


# Custom 404 Error
@app.errorhandler(404)
def custom_error_notfound(error):
    return jsonify({"message": "Page not Found"}), 404


@app.route("/")
def index():
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True)
