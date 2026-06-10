from datetime import datetime
import os

def generate_log(data):
    # STEP 1: Validate input
    if not isinstance(data, list):
        raise ValueError("Input data must be a list")

    # STEP 2: Generate a filename with today's date
    date_str = datetime.now().strftime("%Y%m%d")
    filename = f"log_{date_str}.txt"

    # STEP 3: Write the log entries to a file using File I/O
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: Print a confirmation message with the filename
    print(f"Log written to {filename}")
    
    # CRITICAL: Return the filename so the test file fixtures can read and track it
    return filename