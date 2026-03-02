import os
import requests
from datetime import datetime

def generate_log(data):
    """Writes a list of strings to a timestamped log file."""
    # STEP 1: Validate input
    if not isinstance(data, list):
        raise ValueError("Input data must be a list")
    
    # STEP 2: Generate a filename with today's date
    today = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today}.txt"

    # STEP 3: Write the log entries to a file using File I/O
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: Print a confirmation message
    print(f"Log written to {filename}")

    # Return filename so the autograder tests can verify and clean it up
    return filename

def fetch_data():
    """Fetches data from a public API."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}

# Modular execution block
if __name__ == "__main__":
    # Fetch data using the installed requests package
    post = fetch_data()
    post_title = post.get("title", "No title found")
    print(f"Fetched Post Title: {post_title}")

    # Prepare data to log
    log_data = [
        "User logged in", 
        f"Fetched Post Title: {post_title}", 
        "Report exported"
    ]

    # Generate the log file
    generate_log(log_data)