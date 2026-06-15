from datetime import datetime
import os

def generate_log(data):
    from datetime import datetime

def generate_log(data):
    # STEP 1: Validate input
    # Check if data is a list
    if not isinstance(data, list):
        raise ValueError("Input must be a list")

    # STEP 2: Generate a filename with today's date (e.g., "log_20250408.txt")
    today = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today}.txt"

    # STEP 3: Write the log entries to a file using File I/O
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: Print a confirmation message with the filename
    print(f"Log file '{filename}' has been created successfully.")

    return filename
    
    # Example log generation
    log_data = ["User logged in", f"Fetched post: {post.get('title')}", "Report exported"]
    generate_log(log_data)

