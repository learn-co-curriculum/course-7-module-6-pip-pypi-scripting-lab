from datetime import datetime
import os


def generate_log(data):
    # STEP 1: Validate input
    if not isinstance(data, list):
        raise ValueError("Input data must be a list")

    # STEP 2: Generate a filename with today's date
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # STEP 3: Write the log entries to a file
    with open(filename, "w", encoding="utf-8") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: Print a confirmation message
    print(f"Log written to {filename}")

    return filename
