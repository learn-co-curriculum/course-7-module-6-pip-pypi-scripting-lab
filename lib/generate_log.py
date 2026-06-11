from datetime import datetime
import os

def generate_log(log_data):
    # 1. Autotest: The function raises a ValueError when called with invalid input
    if not isinstance(log_data, list):
        raise ValueError("log_data must be a list")
    
    # 2. Autotest: filename follows pattern log_YYYYMMDD.txt
    today = datetime.now().strftime('%Y%m%d')
    filename = f"log_{today}.txt"
    
    # 3. Autotest: File contents exactly match the input list
    # 4. Autotest: An empty list still creates a valid empty log file
    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")
    
    # 5. Autotest: Function prints a confirmation message including the filename
    print(f"Log written to {filename}")
    
    # 6. Autotest: Returns filename so tests can remove it
    return filename

# For Step 4 of the lab: Use requests + if __name__ == "__main__"
if __name__ == "__main__":
    import requests
    
    def fetch_data():
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        if response.status_code == 200:
            return response.json()
        return {}
    
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))
    
    # Example: also generate a log from the API data
    generate_log([f"API call made", f"Title: {post.get('title', '')}"])