# Project Report

---

##  Website Chosen: [BooksToScrape.com](http://books.toscrape.com)

We chose **Books to Scrape** as our target website because it is designed specifically for educational scraping purposes. The HTML structure is clean, predictable, and consistent across pages. This allowed us to implement advanced scraping techniques such as CSS selectors, parent-child relationships, and relative URL resolution without needing to handle JavaScript or login logic. The site is static, making it a safe and realistic sandbox for beginner to intermediate scraping workflows.

---

##  Project Overview and Implementation

The project was built using Python and BeautifulSoup. It is structured modularly, with clear division of responsibility among modules:

- `scraper/collector.py`: Handles HTTP requests, headers, and pagination
- `scraper/parser.py`: Extracts product data from HTML using BeautifulSoup and CSS selectors
- `models/data_models.py`: Defines a `Book` class to model product data using OOP
- `utils/file_handler.py`: Saves and reloads data from CSV and JSON
- `utils/analyzer.py`: Performs simple analysis like filtering high-priced books and 5-star reviews

The script extracts the following product data:
- Title
- Price (in float format)
- Availability (e.g., “In stock (22 available)”)
- Star rating (e.g., “Four”)
- Product URL

The scraper supports pagination (tested with 2 pages) and can be configured to scrape more. Data is cleaned before export, with price strings converted to floats and whitespace stripped from all fields.

---

##  Implementation Challenges

### 1. URL resolution:
Initially, the product detail links were concatenated manually, causing `404 Not Found` errors. We fixed this using Python’s `urljoin()` to safely combine base and relative URLs.

### 2. CSS-based star rating:
The star rating was stored as part of a class name (e.g., `<p class="star-rating Three">`). We had to extract the second class name programmatically.

### 3. Error handling and robustness:
Some books had missing data or malformed tags. We wrapped parsing logic in `try/except` blocks and provided fallbacks for missing fields.

### 4. Pagination:
We had to extract the "Next" button link using a CSS selector and build the correct next-page URL relative to the current page. We implemented a loop with a limit (`max_pages=2`) and added delay support if extended.

---

##  Data Analysis

From 2 pages (~40 books), we performed basic analysis:

- **Books over £50**: 3
- **Books with 5-star rating**: 7

This revealed that the dataset is reasonably diverse, with a mix of cheap and expensive titles and varied ratings.

---

##  Learning Outcomes

- Learned how to use `BeautifulSoup.select()` and `find_all()` with complex selectors
- Practiced working with structured data models and OOP in a scraping context
- Gained confidence with modular Python packaging and imports
- Understood how to handle broken links, malformed HTML, and optional data
- Strengthened collaboration using GitHub features like branches, PRs, and tags

---

##  Potential Improvements

- Scrape **all pages** using dynamic pagination logic
- Add support for full product descriptions by visiting detail pages
- Add CLI arguments for configuring number of pages, filters, or export format
- Create visualizations using Matplotlib or Seaborn
- Extend the Book model to include image URLs and categories

---

##  Conclusion

We successfully built a complete, object-oriented web scraping application using real-world best practices:
- Clean, maintainable code structure
- Robust error handling and modular design
- Real-time scraping with analysis and data export

The GitHub repository has been tagged as `midterm-submission` and includes full documentation and outputs for review.