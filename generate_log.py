from datetime import datetime
import requests


def fetch_data():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    if response.status_code == 200:
        return response.json()

    return {}


def generate_log(entries):
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in entries:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")


if __name__ == "__main__":
    post = fetch_data()

    log_entries = [
        "User logged in",
        "User updated profile",
        post.get("title", "No title found")
    ]

    generate_log(log_entries)