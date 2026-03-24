import requests
from datetime import datetime
import os

def generate_log(data):
    
    if not isinstance(data, list):
        raise ValueError("Input must be a list")
    
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")
    
    print(f"Log written to {filename}")

    return filename

def fetch_data():
    """Fetching a sample post from a public API"""
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

    if response.status_code == 200:
        return response.json()
    
    return {}

if __name__ == "__main__":

    post = fetch_data()

    log_entries = [
        "User logged in",
        "User updated profile",
        f"Fetched Post Title: {post.get('title', 'No title found')}"
    ]

    generate_log(log_entries)
    