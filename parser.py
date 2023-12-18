import requests as req
from bs4 import BeautifulSoup as bs


def parse(url):
    r = req.get(url)
    html = bs(r.content, "html.parser")
    d = {}  # словарь, содержит информацию о книгах в виде название книги:ее цена
    for i in html.select("article.product_pod"):
        title = i.select("h3")[0].a['title']
        price = i.select(".price_color")[0].text
        d[title] = price
    return d