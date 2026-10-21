import argparse
import requests
from datetime import datetime


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


def write_log(data):
    """Write API data to a text file."""
    filename = f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write("AUTOMATION TOOL LOG\n")
        file.write(f"Generated: {datetime.now()}\n")

        if data:
            file.write(f"Post ID: {data.get('id')}\n")
            file.write(f"User ID: {data.get('userId')}\n")
            file.write(f"Title: {data.get('title')}\n")
            file.write(f"Body: {data.get('body')}\n")
        else:
            file.write("No data was retrieved.\n")

    print(f"Log written to {filename}")


def main():
    parser = argparse.ArgumentParser(
        description="Fetch API data and save it to a file."
    )
    parser.add_argument(
        "--fetch",
        action="store_true",
        help="Fetch data and write it to a log file."
    )
    args = parser.parse_args()

    if args.fetch:
        data = fetch_data()
        write_log(data)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
