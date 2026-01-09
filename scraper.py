import requests
from bs4 import BeautifulSoup

def fetch_news(url):
    """Fetches news headlines from a given URL"""
    try:
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, 'html.parser')
        headlines = [tag.text.strip() for tag in soup.select('.titleline a')[:5]]
        return headlines
    except Exception as e:
        return [f"Error fetching news: {e}"]

def fetch_jobs(url):
    """Fetches job listings from a given URL"""
    try:
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, 'html.parser')
        jobs = [tag.text.strip() for tag in soup.select('.listing-company-name')[:5]]
        return jobs
    except Exception as e:
        return [f"Error fetching jobs: {e}"]
