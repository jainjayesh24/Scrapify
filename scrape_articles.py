import pandas as pd
import requests
from newspaper import Article

# Read CSV
csv_file = "Input.csv"
df = pd.read_csv(csv_file)

article_texts = {}

for index, row in df.iterrows():
    url = row["URL"]
    print(f"Fetching: {url}")

    try:
        article = Article(url)
        article.download()
        article.parse()
        article_texts[url] = article.text
        print(f" Successfully scraped: {url[:50]}...")

    except Exception as e:
        print(f" Failed to extract: {url} | Error: {e}")

# Save to file
with open("articles.txt", "w", encoding="utf-8") as f:
    for url, text in article_texts.items():
        f.write(f"URL: {url}\n{text}\n\n")

print("Scraping complete! Articles saved to articles.txt.")
