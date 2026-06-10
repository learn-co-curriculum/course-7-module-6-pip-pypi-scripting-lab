from datetime import datetime
import requests

log_data = ["User logged in", "User updated profile", "Report exported"]

filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

def write_logs():
    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")


def fetch_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}


if __name__ == "__main__":
    write_logs()
    post = fetch_data()
    print(post.get("title"))
