import sqlite3
from pages_db import PAGES_DB

if __name__ == '__main__':
    new_request = PAGES_DB()
    conn = sqlite3.connect('site.db')
    cur = conn.cursor()
    new_request.create_table(conn, cur)
    new_request.insert_line(conn, cur, 'http://rambler.com', 'Hello!')
    sor = new_request.get_pages(cur)
    new_request.print_pages(sor)
