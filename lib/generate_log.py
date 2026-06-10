from datetime import datetime
import os

def generate_log(data):
    # Validate input
    if not isinstance(data, list):
        raise ValueError("data must be a list")

    # Generate filename using today's date
    today = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today}.txt"

    # Write entries to the file (one per line)
    with open(filename, "w", encoding="utf-8") as f:
        for entry in data:
            f.write(f"{entry}\n")

    # Print confirmation and return filename
    print(f"Log written to {filename}")
    return filename