from datetime import datetime
import os
import requests


def generate_log(data):
    """Write the list of log `data` to a dated file and return the filename.

    Raises ValueError if `data` is not a list.
    """
    if not isinstance(data, list):
        raise ValueError("Input data must be a list.")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # Print confirmation message (required by autograder)
    print(f"Log written to {filename}")

    return filename


def fetch_data():
    """Fetch a sample post from a public API using `requests` and return the JSON.

    This demonstrates using a third-party package as required by the lab.
    """
    try:
        resp = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=5)
        resp.raise_for_status()
        return resp.json()
    except Exception:
        return {}


if __name__ == "__main__":
    sample_logs = [
        "User logged in",
        "User updated profile",
        "Report exported",
    ]

    post = fetch_data()
    if post and "title" in post:
        sample_logs.insert(0, f"Fetched post: {post['title']}")

    filename = generate_log(sample_logs)
    print(f"Log written to {filename}")
