import requests
from bs4 import BeautifulSoup
import sqlite3

# Define the target website
URL = "https://www.artificialintelligence-news.com/"  # Change this to your target site

# Fetch the webpage
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

# Extract articles with proper filtering
articles = set()  # Use a set to avoid duplicates
ignored_titles = {"Subscribe", "Resources", "Events", "Categories", "Join our Community", "Explore"}

for item in soup.find_all("h2"):  # Adjust selector if needed
    title = item.text.strip()
    link = item.a["href"] if item.a and "http" in item.a["href"] else None

    # Store only articles with valid links and avoid generic/irrelevant titles
    if title and link and title not in ignored_titles:
        articles.add((title, link))  # Using set to remove duplicates

# Debugging: Print cleaned articles
print(f"✅ Filtered Articles: {articles}")

# Stop execution if no valid articles found
if not articles:
    print("❌ No valid articles found! Check website structure.")
    exit()

# Save to SQLite database (Avoid duplicates)
conn = sqlite3.connect("articles.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS news (title TEXT UNIQUE, link TEXT UNIQUE)")
for article in articles:
    cursor.execute("INSERT OR IGNORE INTO news VALUES (?, ?)", article)  # Avoid inserting duplicates
conn.commit()
conn.close()

print("✅ Cleaned Data Saved Successfully!")

