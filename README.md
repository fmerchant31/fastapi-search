# FastAPI Search

## Project Overview
FastAPI Search is a simple web scraping and search application built using FastAPI. The application scrapes articles from a website, stores them in a SQLite database, and provides an API to search and retrieve the articles.

### Features
- Web scraping using BeautifulSoup
- Data storage in SQLite database
- REST API using FastAPI
- Search articles by keyword
- Deployed on Railway

## Live Demo
Visit the deployed application: [FastAPI Search on Railway](https://fastapi-search-production.up.railway.app/articles)

## Prerequisites
- Python 3.x
- Virtual environment tool (like venv)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/fmerchant31/fastapi-search.git
   ```
2. Navigate to the project directory:
   ```bash
   cd fastapi-search
   ```
3. Create and activate a virtual environment:
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Scraper
To scrape articles and store them in the database:
```bash
python scraper.py
```

## Starting the API Server
Run the FastAPI server locally:
```bash
uvicorn api:app --host 0.0.0.0 --port 8000
```

## API Endpoints
- **Retrieve all articles:**
  ```http
  GET /articles
  ```
- **Search for articles by keyword:**
  ```http
  GET /search?q=<keyword>
  ```

## Deployment
The application is deployed on Railway. Visit the deployed API at the following link:
[FastAPI Search on Railway](https://fastapi-search-production.up.railway.app/articles)

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue.

## License
This project is licensed under the MIT License.

## Contact
For any inquiries, reach out to Fatema Merchant at fmerchant31@gmail.com.

# fastapi-search
