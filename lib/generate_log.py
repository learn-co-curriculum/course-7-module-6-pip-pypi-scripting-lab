import os
from datetime import datetime
import requests  # Third-party package to satisfy Task 1 & Task 2

def fetch_data():
    """Fetches data from a public API (Task 1: Collect data)."""
    url = "https://jsonplaceholder.typicode.com/posts/1"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
    return {}

def generate_log_file():
    """Combines hardcoded log entries with API data and writes to a file (Task 2 & 3)."""
    # Base data from assignment step 2
    log_data = [
        "User logged in", 
        "User updated profile", 
        "Report exported"
    ]
    
    # Fetch live data from the third-party API
    api_data = fetch_data()
    
    # Process data and add the fetched post title to our log lists
    if api_data and "title" in api_data:
        log_data.append(f"Fetched Post Title: {api_data.get('title')}")
    else:
        log_data.append("Fetched Post Title: No title found")
        
    # Dynamic filename: log_YYYYMMDD.txt
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    
    # Write results using File I/O
    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")
            
    print(f"Log written to {filename}")
    return filename

# Wrap script logic inside the if __name__ == "__main__" block for command-line execution
if __name__ == "__main__":
    generate_log_file()