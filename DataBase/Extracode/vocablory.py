import requests
from bs4 import BeautifulSoup

class VocabularyScraper:
    def __init__(self, url):
        self.url = url

    def scrape(self, str):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all the vocabulary words on the page
        words = []
        def_ = []
        for word in soup.find_all('h2', class_='word-header-txt'):
            words.append(word.text)

        for define in soup.find('p'):
            def_.append(define.text)

        if str == 'w':
            return words
        elif str == 'd':
            return def_

# Define the URL of the vocabulary page
url = 'https://www.merriam-webster.com/word-of-the-day'

# Create a vocabulary scraper
scraper = VocabularyScraper(url)

# Scrape the vocabulary words
words = scraper.scrape('w')
defe = scraper.scrape('d')

# Save the vocabulary words to a file
with open('vocabulary word.txt', 'w') as f:
    for word in words:
        f.write(word)

with open('vocabulary def.txt', 'w') as f:
    for def_ in defe:
        f.write(def_)