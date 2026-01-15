from src.fetch_news import fetch_rss_articles
from src.extract_article import extract_text
from src.summarize import summarize_text

RSS_FEED = "https://feeds.bbci.co.uk/news/rss.xml"

def main():
    articles = fetch_rss_articles(RSS_FEED)
    
    for i, article in enumerate(articles,1):
        print(f"\n{i} {article['title']}")
        text = extract_text(article["link"])

        if len(text) < 500:
            print("Article too short to summarize.")
            continue
        
        summary = summarize_text(text)
        print(summary)

if __name__ == "__main__":
    main()