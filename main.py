from scraper import fetch_news, fetch_jobs
from intent_engine import detect_intent
from datastore import save, read
from config import NEWS_URL, JOBS_URL

def run_chatbot():
    print("Real-Time Chatbot (Web Scraping + NLP)")
    print("Type 'exit' to quit")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        
        intent = detect_intent(user_input)
        
        if intent == "news":
            data = fetch_news(NEWS_URL)
            save("news", data)
            print("Latest News:")
            for item in read("news"):
                print("-", item)
        
        elif intent == "jobs":
            data = fetch_jobs(JOBS_URL)
            save("jobs", data)
            print("Latest Jobs:")
            for item in read("jobs"):
                print("-", item)
        
        else:
            print("Chatbot: Please ask about news or jobs.")

if __name__ == "__main__":
    run_chatbot()
