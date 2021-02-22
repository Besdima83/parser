import sqlite3
from datetime import datetime
from operator import itemgetter


def create_table(connection, cursor):
    cursor.execute("""CREATE TABLE IF NOT EXISTS pages(
       page_id INTEGER PRIMARY KEY AUTOINCREMENT,
       url VARCHAR(255),
       text TEXT,
       parse_time DATE);
    """)
    connection.commit()


def insert_line(connection, cursor, url, text):
    cursor.execute("SELECT COUNT(*) FROM pages WHERE url LIKE '%s'" % url)
    num_url = cursor.fetchone()
    if num_url[0] < 1:
        cursor.execute("""INSERT INTO  pages(url, text, parse_time)
                    VALUES (?, ?, ?);""", (url, text, datetime.now()))
    connection.commit()


def print_table(cursor, name_table):
    cursor.execute(f"SELECT * FROM {name_table}")
    table_rows = cursor.fetchall()
    sort_table_rows = sorted(table_rows, key=itemgetter(3), reverse=True)
    for sort_table_row in sort_table_rows:
        print(sort_table_row)


if __name__ == '__main__':
    conn = sqlite3.connect('site.db')
    cur = conn.cursor()
    create_table(conn, cur)
    insert_line(conn, cur, 'http://mail.com', 'Hello!')
    print_table(cur, 'pages')
