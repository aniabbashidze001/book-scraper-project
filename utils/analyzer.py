def count_expensive_books(books, threshold=50.0):
    return len([book for book in books if float(book["price"]) > threshold])

def list_books_by_rating(books, rating="Five"):
    return [book for book in books if book["rating"] == rating]
