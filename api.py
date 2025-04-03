from fastapi import FastAPI
import sqlite3
import os

app = FastAPI()
DB_PATH = "articles.db"

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

# Call the initialization function when the app starts
initialize_db()

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

