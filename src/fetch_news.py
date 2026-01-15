import requests
from bs4 import BeautifulSoup

def fetch_rss_articles(rss_url, limit = 5):
    response = requests.get(rss_url)

    soup = BeautifulSoup(response.content,"xml")

    articles = []
    for item in soup.find_all("item")[:limit]:
        articles.append(
            {
                "title":item.title.text,
                "link":item.link.text
            }

        )
    return articles


