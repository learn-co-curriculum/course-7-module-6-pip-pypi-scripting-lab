import requests

from lib.generate_log import generate_log


__all__ = ["generate_log", "fetch_data"]


def fetch_data():
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
        f"Fetched post title: {title}",
        "Report exported",
    ]
    generate_log(log_data)