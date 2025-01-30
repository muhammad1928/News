
from bs4 import BeautifulSoup
import requests

def scrape_news():
    url = "https://www.bbc.com/news"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    news = []
    for item in soup.find_all('h3'):
        news.append(item.get_text())
    return news


print(scrape_news())