from datetime import datetime
import requests


def fetch_data():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    if response.status_code == 200:
        return response.json()

    return {}


def generate_log(post):
    log_data = [
        "User logged in",
        "User updated profile",
        "Report exported",
        f"Fetched Post Title: {post.get('title', 'No title found')}"
    ]

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    return filename


if __name__ == "__main__":
    post = fetch_data()

    filename = generate_log(post)

    print(f"Log written to {filename}")