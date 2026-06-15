import os
import requests
from datetime import datetime


def generate_log(log_data):
    if not isinstance(log_data, list):
        raise ValueError("Input must be a list")
    
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    
    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")
    
    print(f"Log written to {filename}")
    return filename


def fetch_data():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1"
    )
    if response.status_code == 200:
        return response.json()
    return {}


if __name__ == "__main__":
    post = fetch_data()
    log_data = [
        "User logged in",
        "User updated profile",
        "Report exported",
        f"Fetched Post Title: {post.get('title', 'No title found')}"
    ]
    generate_log(log_data)