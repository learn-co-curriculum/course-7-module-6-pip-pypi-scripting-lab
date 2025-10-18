from datetime import datetime
import os

def generate_log(data):
    """Generate a log file from a list of entries and return the filename."""

    # STEP 1: Validate input
    if not isinstance(data, list):
        raise ValueError("Input data must be a list.")

    # STEP 2: Create filename using today's date (e.g. log_20251017.txt)
    today = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today}.txt"

    # STEP 3: Write each entry to the file, one per line
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: Print confirmation message
    print(f"Log written to {filename}")

    # STEP 5: Return filename (so tests can verify it)
    return filename
