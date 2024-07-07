from scraper import ContentScraper
from database import DatabaseHandler


def main():
    urls = [
        'https://tecsidel.com'
        ]
    scraper = ContentScraper(urls)
    content = scraper.fetch_content()

    db = DatabaseHandler()
    for data in content:
        db.insert_content(data)
        print(data)

    db.close_connection()


if __name__ == '__main__':
    main()
