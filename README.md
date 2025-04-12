# 📚 Book Scraper Project

This is a web scraping application which collects data from [BooksToScrape](http://books.toscrape.com), processes the HTML content, extracts structured product data, and saves it into both CSV and JSON formats.

## ✅ Features

- Collects product info: title, price, availability, rating, URL
- Scrapes multiple pages with pagination
- Uses Object-Oriented Programming (OOP)
- Cleans, stores, and reloads structured data
- Performs basic analysis (e.g. count of expensive books)
- Modular Python package structure

## 🔧 Setup Instructions

### 1. Clone the repo:
```bash
git clone https://github.com/YOUR-TEAM/book-scraper-project.git
cd book-scraper-project
```

### 2. Install requirements:
```bash
pip install -r requirements.txt
```

### 3. Run the scraper:
```bash
python main.py
```

Outputs will be saved to the `data/` directory as:
- `books.csv`
- `books.json`

## 📂 Project Structure

```
project/
├── main.py
├── scraper/
│   ├── collector.py
│   └── parser.py
├── models/
│   └── data_models.py
├── utils/
│   ├── file_handler.py
│   └── analyzer.py
├── data/
├── requirements.txt
├── README.md
├── CONTRIBUTIONS.md
└── REPORT.md
```

## 📌 Notes

- Target site: http://books.toscrape.com
- For testing purposes we scraped up to 2 pages (adjustable)
- Handles network and parsing errors gracefully