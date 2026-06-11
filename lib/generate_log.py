from datetime import datetime
import os
import argparse

def generate_log(data):
    # Validate input
    if not isinstance(data, list):
        raise ValueError("data must be a list")

    # Generate filename with today's date
    today = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today}.txt"

    # Write entries to file (create empty file for empty list)
    with open(filename, "w", encoding="utf-8") as f:
        for entry in data:
            f.write(f"{entry}\n")

    # Confirmation and return
    print(f"Log written to {filename}")
    return filename


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a dated log file from provided entries")
    parser.add_argument("-e", "--entry", action="append", help="Log entry (can be provided multiple times)")
    parser.add_argument("-f", "--file", help="Path to a text file with one log entry per line")
    args = parser.parse_args()

    entries = []
    if args.file:
        if os.path.exists(args.file):
            with open(args.file, "r", encoding="utf-8") as fh:
                entries.extend([line.rstrip("\n") for line in fh.readlines()])
        else:
            print(f"Specified file not found: {args.file}")
            raise SystemExit(1)

    if args.entry:
        entries.extend(args.entry)

    if not entries:
        entries = [f"Log generated at {datetime.now().isoformat()}"]

    generate_log(entries)
