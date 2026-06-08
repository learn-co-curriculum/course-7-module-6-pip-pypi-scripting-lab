import os
from datetime import datetime
import requests

def fetch_data():
    """Fetches data from a public API using the requests library."""
    url = "https://jsonplaceholder.typicode.com/posts/1"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
    return {}

def write_log_summary(api_data):
    """
    Combines static log data and fetched API data, 
    then writes it to a timestamped file using built-in File I/O.
    """
    # Sample logs from Step 2 instructions
    log_entries = [
        "User logged in", 
        "User updated profile", 
        "Report exported"
    ]
    
    # Extract titles or details from the API response to process the data
    if api_data and "title" in api_data:
        log_entries.append(f"Fetched Post Title: {api_data.get('title')}")
    else:
        log_entries.append("Fetched Post Title: No title found")
        
    # Generate dynamic filename based on current date (YYYYMMDD)
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    
    # Write to file
    with open(filename, "w") as file:
        for entry in log_entries:
            file.write(f"{entry}\n")
            
    print(f"Log successfully written to {filename}")

if __name__ == "__main__":
    print("Starting modular automation tool...")
    
    # Step 1: Collect/Process data from third-party API
    data = fetch_data()
    
    # Step 2: Write results to output files using File I/O
    write_log_summary(data)