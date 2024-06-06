import sqlite3


DATABASE = "books_management.sqlite"

db_connection = sqlite3.connect(DATABASE)
cursor = db_connection.cursor()

CREATE_BOOKS_TABLE = """CREATE TABLE IF NOT EXISTS `books`(
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `author` TEXT NOT NULL,
    `title` TEXT NOT NULL
) """

cursor.execute(CREATE_BOOKS_TABLE)
