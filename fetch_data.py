import requests


def fetch_data():
    """Fetch a post from a public API."""

    url = "https://jsonplaceholder.typicode.com/posts/1"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return {}


def save_to_file(post):
    """Save the fetched post to a text file."""

    with open("post.txt", "w", encoding="utf-8") as file:
        file.write(f"Title: {post.get('title', 'No title found')}\n")
        file.write(f"Body: {post.get('body', 'No body found')}\n")


def main():
    """Main program logic."""

    post = fetch_data()

    if post:
        print("Fetched Post Title:", post.get("title", "No title found"))
        save_to_file(post)
        print("Post saved to post.txt")
    else:
        print("Failed to fetch post data.")


if __name__ == "__main__":
    main()
