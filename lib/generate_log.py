from datetime import datetime
import requests

def generate_log(log_data):
    """
    Creates a log file with timestamped filename log_YYYYMMDD.txt
    """
    # Test 4: raise ValueError for non-list
    if not isinstance(log_data, list):
        raise ValueError("log_data must be a list of strings")

    # Test 1 & 2: timestamped filename log_YYYYMMDD.txt
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # Test 3 & 5: contents match input, empty list creates empty file
    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    # Test 6: prints confirmation with filename
    print(f"Log written to {filename}")
    return filename

def fetch_data():
    """Uses pip-installed requests package - Step 4 of lab"""
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=10)
        if response.status_code == 200:
            return response.json()
        return {}
    except requests.RequestException:
        return {}

if __name__ == "__main__":
    # Default data for command-line execution
    log_data = ["User logged in", "User updated profile", "Report exported"]
    
    # Generate log file
    generate_log(log_data)

    # Use external package
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))