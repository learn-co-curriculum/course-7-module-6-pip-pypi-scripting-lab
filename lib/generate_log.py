import requests
from datetime import datetime

def generate_log(log_data):
    """Generate a log file based on the provided data."""
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    
    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")
    
    print(f"Log written to {filename}")
    return filename  # Return the filename for potential tests

def fetch_data():
    """Fetch data from a public API."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}
