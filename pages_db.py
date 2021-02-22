from datetime import datetime


class PAGES_DB:

    def create_table(self, connection, cursor):
        cursor.execute("""CREATE TABLE IF NOT EXISTS pages(
           page_id INTEGER PRIMARY KEY AUTOINCREMENT,
           url VARCHAR(255),
           text TEXT,
           parse_time DATE);
        """)
        connection.commit()

    def insert_line(self, connection, cursor, url, text):
        cursor.execute("SELECT COUNT(*) FROM pages WHERE url=?", (url,))
        num_url = cursor.fetchone()
        if num_url[0] == 0:
            cursor.execute("""INSERT INTO  pages(url, text, parse_time)
                        VALUES (?, ?, ?);""", (url, text, datetime.now()))
        connection.commit()

    def get_pages(self, cursor):
        cursor.execute("SELECT * FROM pages ORDER BY parse_time DESC")
        sor = cursor.fetchall()
        return sor

    def print_pages(self, name_table):
        for name_tabl in name_table:
            print(name_tabl)

