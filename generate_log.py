import requests
from datetime import datetime


def fetch_data():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    if response.status_code == 200:
        return response.json()

    return {}


def generate_log(post):
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        file.write("Automation Tool Log\n")
        file.write("===================\n")
        file.write(f"Title: {post.get('title', 'No title found')}\n")
        file.write(f"Body: {post.get('body', 'No body found')}\n")

    return filename


if __name__ == "__main__":
    post = fetch_data()

    if post:
        filename = generate_log(post)
        print(f"Log written to {filename}")
    else:
        print("Failed to fetch data.")