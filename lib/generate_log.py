from datetime import datetime
import os

def generate_log(data):
    # STEP 1: Validate input
    if not isinstance(data, list):
        raise ValueError("data must be a list of strings")
    if not all(isinstance(entry, str) for entry in data):
        raise ValueError("all entries in data must be strings")

    # STEP 2: filename
    today_str = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today_str}.txt"

    # STEP 3: write
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: confirm
    print(f"Log written to {filename}")

    # NEW: return for tests
    return filename