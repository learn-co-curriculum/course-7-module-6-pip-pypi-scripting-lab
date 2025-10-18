import requests

def fetch_data():
    """Fetch demo post data from JSONPlaceholder API."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}

if __name__ == "__main__":
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))