from datetime import datetime
import requests


def generate_log(log_data):
    # Input must be a list
    if not isinstance(log_data, list):
        raise ValueError("log_data must be a list")

    # Create filename using today's date
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # Write each item from the list to the file
    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    # Confirmation message
    print(f"Log written to {filename}")


def fetch_data():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    if response.status_code == 200:
        return response.json()

    return {}


if __name__ == "__main__":
    log_data = [
        "User logged in",
        "User updated profile",
        "Report exported"
    ]

    # Use the third-party requests package
    post = fetch_data()

    if post:
        print(
            "Fetched Post Title:",
            post.get("title", "No title found")
        )

    # Generate the log file
    generate_log(log_data)