"""Simple in-memory datastore for CRUD operations"""

store = {
    "news": [],
    "jobs": []
}

def save(category, data):
    """Saves data to the specified category"""
    store[category] = data

def read(category):
    """Reads data from the specified category"""
    return store.get(category, [])

def clear(category):
    """Clears data in the specified category"""
    store[category] = []
