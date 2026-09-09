from datetime import datetime
import requests


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


def generate_log():
    log_data = ["User logged in", "User updated profile", "Report exported"]
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")


if __name__ == "__main__":
    generate_log()
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))