from datetime import datetime

import requests


def generate_log(data):
    """Generate a timestamped log file from a list of entries."""

    # Validate input
    if not isinstance(data, list):
        raise ValueError("Log data must be provided as a list.")

    # Generate filename with today's date
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # Write log entries to the file
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # Print confirmation message
    print(f"Log written to {filename}")

    # Return the filename
    return filename


def fetch_data():
    """Fetch a post from the JSONPlaceholder public API."""

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

    generate_log(log_data)

    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))
