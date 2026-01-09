# Chatbot with Web Scraping and NLP

## Overview
An intelligent chatbot that fetches real-time news and job listings using web scraping techniques and keyword-based NLP for dynamic content delivery.

## Key Features

✨ **Intelligent Intent Detection**: Keyword-based NLP engine to understand user queries

🌐 **Real-Time Web Scraping**: Fetches live news headlines and job listings from the web

💾 **In-Memory Datastore**: Simple CRUD operations for fast data retrieval

🎯 **Modular Architecture**: Clean separation of concerns with dedicated modules

⚡ **Fast Response Times**: Optimized for quick query processing

🛡️ **Exception Handling**: Robust error handling for network requests

## Project Highlights

- **Developed intelligent chatbot** that fetches real-time news and job listings using web scraping techniques and keyword-based NLP responses
- **Implemented modular architecture** with exception handling and CRUD operations, achieving fast query response times for dynamic content delivery

## Tech Stack

- **Python 3.x**
- **BeautifulSoup4**: Web scraping and HTML parsing
- **Requests**: HTTP library for making web requests

## Project Structure

```
chatbot-web-scraping-nlp/
├── main.py              # Main chatbot application entry point
├── scraper.py           # Web scraping functions for news and jobs
├── intent_engine.py     # NLP intent detection using keyword matching
├── datastore.py         # In-memory data storage with CRUD operations
├── config.py            # Configuration file for URL endpoints
└── requirements.txt     # Project dependencies
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Harshith-pabbi/chatbot-web-scraping-nlp.git
cd chatbot-web-scraping-nlp
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure URLs in `config.py` with your target news and jobs sources

## Usage

Run the chatbot:
```bash
python main.py
```

Example interactions:
```
You: Show me the latest news
Chatbot: Latest News:
- Headline 1
- Headline 2
...

You: Find job openings
Chatbot: Latest Jobs:
- Job 1
- Job 2
...

You: exit
Chatbot: Goodbye!
```

## Module Details

### main.py
Entry point of the application that runs the chatbot loop, processes user input, and coordinates between different modules.

### scraper.py
Contains web scraping functions:
- `fetch_news(url)`: Scrapes news headlines from specified URL
- `fetch_jobs(url)`: Scrapes job listings from specified URL

### intent_engine.py
Keyword-based intent detection engine that classifies user queries into categories (news, jobs, unknown).

### datastore.py
Simple in-memory datastore with CRUD operations:
- `save(category, data)`: Store data
- `read(category)`: Retrieve data
- `clear(category)`: Clear data

### config.py
Configuration file containing URL endpoints for news and jobs sources.

## Features in Detail

### Intent Detection
The chatbot uses keyword matching to detect user intent:
- **News Intent**: Triggers on keywords like "news", "headlines", "updates"
- **Jobs Intent**: Triggers on keywords like "job", "jobs", "hiring", "career"

### Web Scraping
- Uses BeautifulSoup4 for HTML parsing
- Implements timeout handling for network requests
- Exception handling for failed requests

### Data Management
- In-memory storage for quick access
- Separate storage categories for news and jobs
- Simple CRUD interface

## Customization

### Adding New Intents
Edit `intent_engine.py` and add new keywords to `INTENT_KEYWORDS` dictionary:
```python
INTENT_KEYWORDS = {
    "jobs": ["job", "jobs", "hiring"],
    "news": ["news", "headline", "updates"],
    "weather": ["weather", "forecast"]  # New intent
}
```

### Changing Data Sources
Update URLs in `config.py`:
```python
NEWS_URL = "https://your-news-source.com"
JOBS_URL = "https://your-jobs-source.com"
```

## Future Enhancements

- [ ] Add natural language processing with spaCy or NLTK
- [ ] Implement persistent storage with databases
- [ ] Add more data sources (weather, stocks, etc.)
- [ ] Create web interface with Flask/FastAPI
- [ ] Add sentiment analysis for news
- [ ] Implement caching mechanism

## License

This project is open source and available for educational purposes.

## Author

Harshith Pabbi

---

**Note**: Make sure to update the CSS selectors in `scraper.py` according to your target websites' HTML structure.
