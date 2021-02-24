import sqlite3
from pages_db import PAGES_DB
import requests
from bs4 import BeautifulSoup

URL = 'https://appleinsider.ru'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
    'Accept': '*/*'}


def get_html(url, params=None):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('article')

    news = []
    for item in items:
        title = item.find('h2', class_='entry-title')
        if title:
            title = title
        else:
            continue
        news.append({
            'link_news': title.find('a').get('href'),
            'title': title.get_text().strip(),
            'content': item.find('div',
                                 class_='entry-content').get_text().strip().replace('\n', ' '),

        })

    return news


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        return get_content(html.text)
    else:
        print('Error web host')


if __name__ == '__main__':
    new_request = PAGES_DB()
    conn = sqlite3.connect('site.db')
    cur = conn.cursor()
    new_request.create_table(conn, cur)
    for new_par in parse():
        url = new_par['link_news']
        title = new_par['title']
        text = new_par['content']

        new_request.insert_line(conn, cur, url, title, text)

    sor = new_request.get_pages(cur)
    new_request.print_pages(sor)

