import requests 
from lib.generate_log import generate_log

def fetch_data():
    
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    return {}

if __name__ == "__main__":
    post = fetch_data()

    title = post.get("title,", "no title found")
    log_data = [
        "User logged on"
        f"Fetched post title: {title}",
        "Report Executed"
    ]

    generate_log(log_data)