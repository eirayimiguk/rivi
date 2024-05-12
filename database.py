import os
import sqlite3


def create_connection(database_file):
    connection = None
    try:
        connection = sqlite3.connect(database_file)
        print(f"SQLite: {sqlite3.version}")
    except sqlite3.Error as e:
        print(e)
    return connection


def create_table(connection):
    sql = """
        CREATE TABLE IF NOT EXISTS images(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name STRING NOT NULL UNIQUE,
            like INTEGER DEFAULT 0,
            bad INTEGER DEFAULT 0
        );
    """
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()


def insert_all_images(connection):
    sql = """
        INSERT OR IGNORE INTO images (name) VALUES (?);
    """

    image_files = [
        filename
        for filename in os.listdir("static/images")
        if filename.split(".")[-1].lower() in ["jpg", "jpeg", "png", "webp"]
    ]
    cursor = connection.cursor()
    cursor.executemany(sql, [(filename,) for filename in image_files])
    connection.commit()


def select_all_images(connection):
    sql = """
        SELECT * FROM images;
    """
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def main():
    try:
        connection = create_connection("images.db")
        create_table(connection)
        insert_all_images(connection)
        select_all_images(connection)
    except Exception as e:
        print(e)
    finally:
        connection.close()


if __name__ == "__main__":
    main()
