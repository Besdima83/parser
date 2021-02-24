from datetime import datetime
import sqlite3

NAME_DB = 'site.db'
connection = sqlite3.connect(NAME_DB)
cursor = connection.cursor()


class CreationBD:
    def __init__(self):
        self.create_table()

    def create_table(self):
        cursor.execute("""CREATE TABLE IF NOT EXISTS pages(
           page_id INTEGER PRIMARY KEY AUTOINCREMENT,
           url VARCHAR(255),
           news_title TEXT,
           text TEXT,
           parse_time DATE);
        """)
        connection.commit()

    def insert_line(self, url, news_title, text):
        cursor.execute("SELECT COUNT(*) FROM pages WHERE url=?", (url,))
        num_url = cursor.fetchone()
        if num_url[0] == 0:
            cursor.execute("""INSERT INTO  pages(url, news_title, text, parse_time)
                        VALUES (?, ?, ?, ?);""",
                           (url, news_title, text, datetime.now()))
        connection.commit()


    def print_table_bd(self):
        for name_tabl in cursor.execute("SELECT * FROM pages ORDER BY parse_time DESC"):
            print(name_tabl)
