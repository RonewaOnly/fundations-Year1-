import requests
from bs4 import BeautifulSoup

url = 'https://humornama.com/jokes/fun-fact-of-the-day/'

soup = BeautifulSoup(requests.get(url).content, 'html.parser')

jokes = soup.find_all('div', class_='entry-content')
for joke in jokes:
    print(joke.get_text(strip=True))
    print('---')
# End of WebScraper/Scraper.py
