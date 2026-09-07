from datetime import datetime
import requests


def generate_log(data):
    # Check that data is a list
    if not isinstance(data, list):
        raise ValueError("Data must be a list")

    # Create filename using today's date
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # Write each log entry to the file
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # Print confirmation
    print(f"Log written to {filename}")

    # Return the filename
    return filename


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

    generate_log(log_data)

    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))