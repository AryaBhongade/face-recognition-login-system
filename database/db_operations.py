import sqlite3


def save_user(username, face_encoding):

    connection = sqlite3.connect("database/users.db")

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO users
        (username, face_encoding)
        VALUES (?, ?)
        """,
        (username, face_encoding)
    )

    connection.commit()
    connection.close()