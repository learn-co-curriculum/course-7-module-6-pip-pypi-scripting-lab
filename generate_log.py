"""Top-level wrapper script for running the automation tool.

This mirrors the behavior of `lib/generate_log.py` and allows running:

    python3 generate_log.py

so instructions that expect a root-level script continue to work.
"""
from lib.generate_log import generate_log, fetch_data


def main():
    sample_logs = [
        "User logged in",
        "User updated profile",
        "Report exported",
    ]

    post = fetch_data()
    if post and "title" in post:
        sample_logs.insert(0, f"Fetched post: {post['title']}")

    generate_log(sample_logs)


if __name__ == "__main__":
    main()
