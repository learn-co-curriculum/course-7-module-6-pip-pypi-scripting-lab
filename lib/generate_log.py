import requests
from datetime import datetime

def generate_log(log_data):
    # Make sure we actually get a list before trying to loop through it
    if not isinstance(log_data, list):
        raise ValueError("Input must be a list")

    # Format the date like YYYYMMDD for the text file name
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # Create the file and write each log entry on a new line
    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    # Print a quick success message so we know it worked
    print(f"Log written to {filename}")
    
    return filename

def fetch_data():
    # Grab some dummy data from the public API
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}

# Only run this test code if we execute the script directly
if __name__ == "__main__":
    # Test the API fetcher
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))
    
    # Test the log generator
    sample_logs = ["User logged in", "User updated profile", "Report exported"]
    generate_log(sample_logs)