import requests
import time

def fetch_data(url, retries=3, delay=2):
    """Fetch data from an API with retry mechanism"""
    for attempt in range(retries):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        print(f"Retrying ({attempt + 1}/{retries})...")
        time.sleep(delay)
    return {"error": "Failed to fetch data"}
