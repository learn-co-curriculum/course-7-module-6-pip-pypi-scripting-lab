from datetime import datetime
import os

def generate_log(data):
    """Create a dated log file and return its filename."""
    if not isinstance(data, list):
        raise ValueError("Data must be a list")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")
    return filename
