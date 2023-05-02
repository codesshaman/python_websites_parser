import re
from lxml import etree
import requests
from bs4 import BeautifulSoup


class Get():
    "Класс для функций, обрабатывающих get-запросы"
    def __init__(self, uri):
        super().__init__()

    def get_html(url):
        response = requests.get(url)
        print(response)
        return response.text

    def get_from_file(path):
        with open(path) as file:
            src = file.read()
        return src

    def get_lot_id(html):
        soup = BeautifulSoup(html, 'lxml')
        price = soup.find('span', class_="").text.strip()
        return price


    def get_id(html):
        soup = BeautifulSoup(html, 'lxml')
        id = soup.find('div', class_="registry-entry__header-mid__number").find('a', target="_blank").get('href')
        return id


    def get_id_re(html):
        soup = BeautifulSoup(html, 'lxml')
        id = soup.find('div', class_="registry-entry__header-mid__number")
        id = re.findall(r'href\s*=\s*["\'](.*?)["\']', str(id))
        return id[0]