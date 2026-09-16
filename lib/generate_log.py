from datetime import datetime
import requests

def fetch_data():
    """Fetches sample data from a public REST API using the requests package."""
    try:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/posts/1", timeout=5
        )
        if response.status_code == 200:
            return response.json()
    except requests.RequestException:
        pass
    return {}

def generate_log(log_data):
    """Generates a timestamped log file from a list of log entries.
    Raises a ValueError if input is not a list.
    """
    # Validate that log_data is a list to pass test criteria
    if not isinstance(log_data, list):
        raise ValueError("Input must be a list of log entries.")
    # Format filename according to log_YYYYMMDD.txt pattern
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    # Write log entries to the file (handles empty list safely)
    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")
    # Print required confirmation message containing the filename
    print(f"Log written to {filename}")
    return filename


if __name__ == "__main__":
    # Fetch data using the installed requests package
    post = fetch_data()
    post_title = post.get("title", "No title found")
    print("Fetched Post Title:", post_title)

    # Log the fetched title along with status entries
    sample_data = [
        "User logged in",
        f"Fetched post title: {post_title}",
        "Report exported",
    ]
    generate_log(sample_data)