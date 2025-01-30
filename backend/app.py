import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/news', methods=['GET'])
def get_news():
    api_key = "YOUR_NEWS_API_KEY"
    url = f"https://newsapi.org/v2/top-headlines?language=en&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)


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


@app.route('/api/scraped-news', methods=['GET'])
def scraped_news():
    data = scrape_news()
    return jsonify(data)
