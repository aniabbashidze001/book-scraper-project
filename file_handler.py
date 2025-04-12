import csv
import json
import os

def save_books_to_csv(books, filename="data/books.csv"):
    os.makedirs("data", exist_ok=True)
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=books[0].as_dict().keys())
        writer.writeheader()
        for book in books:
            writer.writerow(book.as_dict())

def save_books_to_json(books, filename="data/books.json"):
    os.makedirs("data", exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump([book.as_dict() for book in books], f, indent=4)

def load_books_from_csv(filename="data/books.csv"):
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)
