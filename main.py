# generate_log.py (project root)
import requests
from lib.generate_log import generate_log


def fetch_data():
    """Fetch a post from a public API."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}


if __name__ == "__main__":
    post = fetch_data()
    title = post.get("title", "No title found")
    print("Fetched Post Title:", title)

    log_data = [
        "User logged in",
        "User updated profile",
        "Report exported",
        f"Fetched API title: {title}",
    ]

    filename = generate_log(log_data)
    print(f"Log written to {filename}")