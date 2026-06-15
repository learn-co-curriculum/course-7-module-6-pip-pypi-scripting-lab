from datetime import datetime
import requests


def fetch_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    

    return None


def generate_log(log_data):
    if not isinstance(log_data, list):
        raise ValueError("log_data must be a list")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    post = fetch_post()

    with open(filename, "w") as file:
        # write logs
        for item in log_data:
            file.write(f"{item}\n")

        # write API data
        file.write("\nAPI DATA\n")
        if post:
            file.write(f"Title: {post.get('title')}\n")
        else:
            file.write("Failed to fetch API data\n")

    print(f"Log written to {filename}")
    return filename


if __name__ == "__main__":
    sample_logs = [
        "User logged in",
        "User updated profile",
        "Report exported"
    ]

    generate_log(sample_logs)