from datetime import datetime
import requests

def generate_log(data):
    if not isinstance(data, list):
        raise ValueError("Data should be a list of log entries.")


    filename= f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, 'w') as file:
        for entry in data:
            file.write(f"{entry}\n")    
    print(f"Log file '{filename}' has been generated successfully.")
    return filename


def fetch_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}


if __name__ == "__main__":
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))
