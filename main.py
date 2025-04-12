from scraper.collector import crawl_multiple_pages
from scraper.parser import parse_books_from_html
from utils.file_handler import save_books_to_csv, save_books_to_json, load_books_from_csv
from utils.analyzer import count_expensive_books, list_books_by_rating

if __name__ == "__main__":
    print("Scraping books from BooksToScrape.com...")

    pages = crawl_multiple_pages("http://books.toscrape.com/", max_pages=2)
    all_books = []

    for html in pages:
        all_books.extend(parse_books_from_html(html))

    print(f"Scraped {len(all_books)} books.")

    save_books_to_csv(all_books)
    save_books_to_json(all_books)

    books_loaded = load_books_from_csv()
    over_50 = count_expensive_books(books_loaded)
    top_rated = list_books_by_rating(books_loaded, "Five")

    print(f"{over_50} books are over £50.")
    print(f"{len(top_rated)} books have a 5-star rating.")
