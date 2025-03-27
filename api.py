from fastapi import FastAPI
import sqlite3

app = FastAPI()

# API Endpoint to get all articles
@app.get("/articles")
def get_articles():
    conn = sqlite3.connect("articles.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM news")
    data = cursor.fetchall()
    conn.close()
    return {"articles": [{"title": row[0], "link": row[1]} for row in data]}

# API Endpoint to search articles by keyword
@app.get("/search")
def search_articles(q: str):
    conn = sqlite3.connect("articles.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM news WHERE title LIKE ?", ('%' + q + '%',))
    data = cursor.fetchall()
    conn.close()
    return {"search_results": [{"title": row[0], "link": row[1]} for row in data]}


