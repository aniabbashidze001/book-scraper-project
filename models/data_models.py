class Book:
    def __init__(self, title, price, availability, rating, url):
        self.title = title
        self.price = price
        self.availability = availability
        self.rating = rating
        self.url = url

    def __str__(self):
        return f"{self.title} - £{self.price} ({self.rating})"

    def as_dict(self):
        return {
            "title": self.title,
            "price": self.price,
            "availability": self.availability,
            "rating": self.rating,
            "url": self.url
        }
