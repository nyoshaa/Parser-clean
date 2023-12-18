from printer import print_results
from parser import parse

URL = "https://books.toscrape.com/catalogue/category/books/classics_6/index.html"


def main():
    data = parse(URL)
    print_results(data)


main()