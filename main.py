from model.getdata import Get
from bs4 import BeautifulSoup

import requests


headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}

url = 'https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searchString=32312329789'


def main(url):
    # for online parsing
    # html = Get.get_html(url)
    # for local parsing
    html = Get.get_from_file("test.html")
    id = Get.get_id(html)
    print(id)
    # print(type(id))
    # default_url = f"https://zakupki.gov.ru{id}"
    # html = Get.get_html(default_url)
    # print(html)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main(url)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
