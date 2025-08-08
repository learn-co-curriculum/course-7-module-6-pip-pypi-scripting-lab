from lib.generate_log import generate_log
import requests

def fetch_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}

if __name__ == "__main__":
    # Fetch a post from the API
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))

    # Create log entries
    log_data = [
        "User logged in",
        "User updated profile",
        "Report exported",
        f"Fetched post title: {post.get('title', 'No title found')}"
    ]
    generate_log(log_data)