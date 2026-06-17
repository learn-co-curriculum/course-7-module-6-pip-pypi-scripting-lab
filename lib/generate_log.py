from datetime import datetime
import requests


API_URL = "https://jsonplaceholder.typicode.com/posts/1"


def fetch_data(url=API_URL):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return {}


def build_log_entries(post):
    return [
        f"Post ID: {post.get('id', 'N/A')}",
        f"Title: {post.get('title', 'No title found')}",
        f"Body: {post.get('body', 'No body found')}",
    ]


def generate_log(data):
    if not isinstance(data, list):
        raise ValueError("data must be a list")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    with open(filename, "w") as file:
        file.write("".join(f"{entry}\n" for entry in data))

    print(f"Log generated: {filename}")
    return filename


def main():
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))
    generate_log(build_log_entries(post))


if __name__ == "__main__":
    main()
