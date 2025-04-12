import requests
import time

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}
BASE_URL = "http://books.toscrape.com/"

def get_page(url):
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def crawl_multiple_pages(start_url, max_pages=2, delay=1):
    pages = [start_url]
    all_html = []

    for i in range(max_pages):
        print(f"Fetching page {i+1}: {pages[-1]}")
        html = get_page(pages[-1])
        if not html:
            break
        all_html.append(html)

        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html, "html.parser")
        next_btn = soup.select_one("li.next > a")
        if next_btn:
            next_url = pages[-1].rsplit("/", 1)[0] + "/" + next_btn["href"]
            pages.append(next_url)
            time.sleep(delay)
        else:
            break

    return all_html
