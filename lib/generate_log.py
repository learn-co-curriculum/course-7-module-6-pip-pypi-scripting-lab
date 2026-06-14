from datetime import datetime
import os
import requests


def fetch_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}


def generate_log(data):
    # STEP 1: Validate input
    if not isinstance(data, list):
        print("Error: data must be a list.")
        return

    # STEP 2: Create filename
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    filepath = os.path.join(os.getcwd(), filename)

    # STEP 3: Write to file
    with open(filepath, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: Confirmation
    print(f"Log file created successfully: {filepath}")


if __name__ == "__main__":
    post = fetch_data()

    # Convert API data into list format (IMPORTANT)
    if post:
        log_data = [
            f"Title: {post.get('title')}",
            f"Body: {post.get('body')}",
            f"User ID: {post.get('userId')}"
        ]
    else:
        log_data = ["No data fetched"]

    generate_log(log_data)