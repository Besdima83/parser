import sqlite3
from pages_db import PAGES_DB
import parser


if __name__ == '__main__':
    new_request = PAGES_DB()
    conn = sqlite3.connect('site.db')
    cur = conn.cursor()
    new_request.create_table(conn, cur)
    parser.add_news_to_db(conn, cur, new_request)
    sor = new_request.get_pages(cur)
    new_request.print_pages(sor)

