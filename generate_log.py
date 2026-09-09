from datetime import datetime
import requests


def generate_log(log_data=None):
    # Set default list if none is passed
    if log_data is None:
        log_data = ["User logged in", "User updated profile", "Report exported"]

    # Requirement 4: Raise ValueError when called with non-list types
    if not isinstance(log_data, list):
        raise ValueError("log_data must be a list of string entries")

    # Requirement 2: Filename pattern log_YYYYMMDD.txt
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # Requirement 3 & 5: Write log contents (creates empty file if log_data is [])
    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    # Requirement 6: Confirmation message including filename
    print(f"Log written to {filename}")

    return filename


def fetch_data():
    try:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/posts/1", timeout=5
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as err:
        print(f"API Request Failed: {err}")
        return {}


if __name__ == "__main__":
    generate_log()
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))