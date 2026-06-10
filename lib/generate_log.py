from argparse import ArgumentParser
from datetime import datetime
from pathlib import Path


DEFAULT_LOG_DATA = ["User logged in", "User updated profile", "Report exported"]
DEFAULT_API_URL = "https://jsonplaceholder.typicode.com/posts/1"


def generate_log(data, output_dir="."):
    """Write log entries to a dated text file and return the filename."""
    if not isinstance(data, list):
        raise ValueError("Log data must be provided as a list.")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    output_path = Path(output_dir) / filename

    with open(output_path, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    print(f"Log written to {output_path}")
    return str(output_path) if output_dir != "." else filename


def fetch_data(url=DEFAULT_API_URL):
    """Fetch JSON data from a public API using the requests package."""
    try:
        import requests
    except ImportError as exc:
        raise ImportError(
            "The requests package is required. Install it with: pip install requests"
        ) from exc

    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        return response.json()
    return {}


def build_log_entries(include_api_title=False, api_url=DEFAULT_API_URL):
    """Build default log entries, optionally including data from the API."""
    entries = DEFAULT_LOG_DATA.copy()

    if include_api_title:
        post = fetch_data(api_url)
        entries.append(f"Fetched Post Title: {post.get('title', 'No title found')}")

    return entries


def main():
    parser = ArgumentParser(description="Generate a dated automation log file.")
    parser.add_argument(
        "--entry",
        action="append",
        dest="entries",
        help="Log entry to write. Repeat this option to add multiple entries.",
    )
    parser.add_argument(
        "--include-api-title",
        action="store_true",
        help="Fetch a sample post title with requests and include it in the log.",
    )
    parser.add_argument(
        "--api-url",
        default=DEFAULT_API_URL,
        help="API URL to fetch when --include-api-title is used.",
    )
    parser.add_argument(
        "--output-dir",
        default=".",
        help="Directory where the generated log file should be saved.",
    )
    args = parser.parse_args()

    entries = args.entries or build_log_entries(args.include_api_title, args.api_url)
    filename = generate_log(entries, args.output_dir)
    print(f"Generated {filename}")


if __name__ == "__main__":
    main()
