from datetime import datetime
import os
import requests

def fetch_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}

def generate_log(data):
    # STEP 1: Validate input
    if not isinstance(data, list):
        raise ValueError("Input must be a list")
    
    # STEP 2: Generate a filename with today's date (e.g., "log_20250408.txt")
    today = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today}.txt"
    
    # STEP 3: Write the log entries to a file using File I/O
    with open(filename, 'w') as file:
        for entry in data:
            file.write(f"{entry}\n")
    
    # STEP 4: Print a confirmation message with the filename
    print(f"Log file created: {filename}")
    
    return filename

if __name__ == "__main__":
    # Fetch data from external API
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))
    
    # Create log with sample data
    log_data = ["User logged in", "User updated profile", "Report exported"]
    filename = generate_log(log_data)
    
    # Add API data to log
    with open(filename, 'a') as file:
        file.write(f"API Data: {post.get('title', 'No title')}\n")
        file.write(f"API Body: {post.get('body', 'No body')}\n")
