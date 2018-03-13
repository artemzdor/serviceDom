#!/usr/bin/python3
# -*- coding: utf-8 -*-

import bs4
import requests

HOST = "http://www.zakupki.gov.ru"
urlSerch = "http://www.zakupki.gov.ru/epz/order/quicksearch/search_eis.html?searchString=реклама"
if __name__ == "__main__":
    page = requests.get(urlSerch)
    print(page.text)