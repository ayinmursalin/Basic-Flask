from flask import Blueprint, request, jsonify

post = Blueprint("post", __name__, url_prefix='/api')


@post.route("/posts", methods=["GET", "POST"])
def posts():
    if request.method == "GET":
        return jsonify({"message": "Success get all Post"})
    
    if request.method == 'POST':
        return jsonify({"message": "Success create new Post"})

    return ""
