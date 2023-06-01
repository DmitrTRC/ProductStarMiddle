"""
1. Do search queries to https://google.com/, getting html page
2. From the html page, get all links (in html it is a construction like <a href=...>)
3. Save this to the sqlite database.
"""

import requests
import sqlite3

from bs4 import BeautifulSoup


class GoogleSearch:

    def __init__(self, search_query):
        self.search_query = search_query

    def get_html(self):
        response = requests.get(f'https://www.google.com/search?q={self.search_query}')
        return response.text

    def get_links(self):
        soup = BeautifulSoup(self.get_html(), 'html.parser')
        links = soup.find_all('a')
        return links

    def save_to_db(self):
        conn = sqlite3.connect('gsearch.db')
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS links (link TEXT)')
        for link in self.get_links():
            cursor.execute('INSERT INTO links VALUES (?)', (link.get('href'),))
        conn.commit()
        conn.close()


if __name__ == '__main__':

    search_query_text = input('Enter search query: ')
    google_search = GoogleSearch(search_query_text)
    google_search.save_to_db()
