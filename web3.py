from bs4 import BeautifulSoup as bs
import requests

URL = "https://www.goodreads.com/book/random"
MIN_RATING_COUNT = 30


def to_float(rating_count):
    """Docstring here."""
    rating = rating_count.split()[0]
    if ',' in rating:
        return float(rating.replace(',', '.'))
    return float(rating)


def format_title(book_title):
    """Docstring here."""
    return ' '.join(book_title.split()).replace('&amp;', '&')


def get_html_source():
    """Docstring here."""
    html_source = requests.get(URL).text
    return bs(html_source, 'html.parser')


def get_book_rating_count(soup):
    """Docstring here."""
    return soup.find('span', attrs={'class', 'value-title'}).get_text()


def get_book_title(soup):
    """Docstring here."""
    return soup.find('h1', attrs={'class': 'bookTitle'}).get_text()


def get_book_pages(soup):
    """Docstring here."""
    return soup.find('span', attrs={'itemprop': 'numberOfPages'}).get_text()


def get_book_rating(soup):
    """Docstring here."""
    return soup.find('span', attrs={'itemprop': 'ratingValue'}).get_text()


def main():
    """Docstring here."""
    while True:
        soup = get_html_source()
        book_rating_count = get_book_rating_count(soup)

        if to_float(book_rating_count) > MIN_RATING_COUNT:
            try:
                book_pages = get_book_pages(soup)
            except AttributeError:
                book_pages = 'No pages available'
            book_title = format_title(get_book_title(soup))
            book_rating = get_book_rating(soup)

            print('Title: {}\n'
                  'Pages: {}\n'
                  'Rating: {}\n\n'.format(book_title, book_pages, book_rating))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("You've decided to close the program")
