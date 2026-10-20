from datetime import datetime
import os


def generate_log(data):
    # Validate input
    if not isinstance(data, list):
        raise ValueError("Input must be a list of log entries.")

    # Filename with today's date
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # Write each entry on its own line
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # Confirmation message
    print(f"Log written to {filename}")

    return filename