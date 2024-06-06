import sqlite3
from flask import Flask, request, jsonify, g
from dbhelper import DATABASE

app = Flask(__name__)


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = make_dicts
    return db


def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value) for idx, value in enumerate(row))


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


@app.route("/")
def index():
    return "Hello World!"


@app.route("/api/books", methods=["GET", "POST"])
def books():
    conn = get_db()

    if request.method == "POST":
        try:
            data = request.get_json()

            cursor = conn.execute(
                "INSERT INTO books (author, title) VALUES (?, ?)",
                (data["author"], data["title"]),
            )
            conn.commit()

            cursor = conn.execute(
                "SELECT * FROM books WHERE id = ?", [str(cursor.lastrowid)]
            )
            book = cursor.fetchone()

            cursor.close()

            return (
                jsonify(
                    {
                        "message": "Successfully create new Book",
                        "data": book,
                    }
                ),
                201,
            )
        except Exception as e:
            conn.rollback()
            return jsonify(f"Unable to create new book - {e}")

    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM books")
        books = cursor.fetchall()

        cursor.close()

        return jsonify(
            {
                "message": "Successfully get List of book",
                "data": books,
            }
        )

    return ""


@app.route("/api/books/<book_id>", methods=["GET", "PUT", "DELETE"])
def book_operation(book_id):
    conn = get_db()

    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM books WHERE id = ?", [book_id])
        book = cursor.fetchone()

        cursor.close()

        if book is None:
            return jsonify({"message": "Unable to get book"}), 404

        return jsonify(
            {
                "message": "Successfully get the book",
                "data": book,
            }
        )

    if request.method == "PUT":
        try:
            data = request.get_json()

            cursor = conn.execute(
                "UPDATE books SET author = ?, title = ? WHERE id = ?",
                [data["author"], data["title"], book_id],
            )
            conn.commit()

            cursor = conn.execute("SELECT * FROM books WHERE id = ?", [book_id])
            updated_book = cursor.fetchone()

            cursor.close()

            return jsonify(
                {
                    "message": "Successfully update the book",
                    "data": updated_book,
                }
            )
        except Exception as e:
            conn.rollback()
            return jsonify(f"Unable to create edit book - {e}")

    if request.method == "DELETE":
        try:
            cursor = conn.execute(
                "DELETE FROM books WHERE id = ?",
                [book_id],
            )
            conn.commit()

            cursor.close()

            return jsonify({"message": "Successfully delete the book"})
        except Exception as e:
            conn.rollback()
            return jsonify(f"Unable to create delete book - {e}")

    return ""


if __name__ == "__main__":
    app.run(debug=True)
