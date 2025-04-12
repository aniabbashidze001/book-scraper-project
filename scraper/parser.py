from bs4 import BeautifulSoup
from models.data_models import Book
from urllib.parse import urljoin

def parse_books_from_html(html_page):
    soup = BeautifulSoup(html_page, "html.parser")
    book_elements = soup.select("article.product_pod")
    books = []

    for element in book_elements:
        title = element.h3.a["title"]
        price = element.select_one("p.price_color").text.strip().replace("£", "")
        availability = element.select_one("p.instock.availability").text.strip()
        rating = element.select_one("p.star-rating")["class"][1]
        relative_url = element.h3.a["href"]
        url = urljoin("http://books.toscrape.com/catalogue/", relative_url)

        try:
            price = float(price)
        except ValueError:
            price = 0.0

        book = Book(title, price, availability, rating, url)
        books.append(book)

    return books
