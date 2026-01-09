"""Intent detection engine using keyword matching"""

INTENT_KEYWORDS = {
    "jobs": ["job", "jobs", "hiring", "career", "opening"],
    "news": ["news", "headline", "updates", "latest"],
}

def detect_intent(user_input: str) -> str:
    """Detects user intent from input text"""
    text = user_input.lower()
    
    for intent, keywords in INTENT_KEYWORDS.items():
        if any(word in text for word in keywords):
            return intent
    
    return "unknown"
