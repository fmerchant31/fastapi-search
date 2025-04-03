from fastapi import FastAPI
import sqlite3
import os
import requests
from bs4 import BeautifulSoup

app = FastAPI()
DB_PATH = "articles.db"
NEWS_URL = "https://news.ycombinator.com/"  # Example source

# Initialize the database if it doesn't exist
def initialize_db():
    if not os.path.exists(DB_PATH):
        conn = sqlite3.connect(DB_PATH)
        conn.execute('''
            CREATE TABLE IF NOT EXISTS news (
                title TEXT,
                link TEXT
            )
        ''')
        conn.commit()
        conn.close()

# Scrape articles and store them in the database
def scrape_and_store():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # Check if the database already has data
    cursor.execute("SELECT COUNT(*) FROM news")
    count = cursor.fetchone()[0]

    if count == 0:  # Only scrape if the database is empty
        response = requests.get(NEWS_URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = []

        # Scrape articles from the news source
        for item in soup.select(".storylink"):
            title = item.get_text()
            link = item.get("href")
            articles.append((title, link))

        # Insert scraped articles into the database
        cursor.executemany("INSERT INTO news (title, link) VALUES (?, ?)", articles)
        conn.commit()

    conn.close()

# Call the initialization and scraping functions when the app starts
initialize_db()
scrape_and_store()

# API Endpoint to get all articles
@app.get("/articles")
def get_articles():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM news")
    data = cursor.fetchall()
    conn.close()
    return {"articles": [{"title": row[0], "link": row[1]} for row in data]}

# API Endpoint to search articles by keyword
@app.get("/search")
def search_articles(q: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM news WHERE title LIKE ?", ('%' + q + '%',))
    data = cursor.fetchall()
    conn.close()
    return {"search_results": [{"title": row[0], "link": row[1]} for row in data]}

