
import argparse
import requests
from lib.generate_log import generate_log


def fetch_data():
    """Fetch a sample post from a public API."""
    url = "https://jsonplaceholder.typicode.com/posts/1"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as error:
        print(f"Error fetching data: {error}")
        return None


def main():
    """Run the automation tool from the command line."""
    parser = argparse.ArgumentParser(
        description="Fetch API data and save it to a log file."
    )
    parser.add_argument(
        "--fetch",
        action="store_true",
        help="Fetch data and write it to a log file."
    )

    args = parser.parse_args()

    if not args.fetch:
        parser.print_help()
        return

    data = fetch_data()

    if data is None:
        entries = ["API request failed; no data retrieved."]
    else:
        entries = [
            f"Post ID: {data.get('id')}",
            f"User ID: {data.get('userId')}",
            f"Title: {data.get('title')}",
            f"Body: {data.get('body')}",
        ]

    filename = generate_log(entries)
    print(f"Log written to {filename}")


if __name__ == "__main__":
    main()
