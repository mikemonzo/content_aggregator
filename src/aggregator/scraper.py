import requests
from bs4 import BeautifulSoup

class ContentScraper:
    def  __init__(self, urls) -> None:
        self.urls = urls

    
    def fetch_content(self):
        content = []
        for url in self.urls:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                content.append(self.parse_content(soup))
        return content
    

    def parse_content(self, soup):
        return soup.get_text()
    
