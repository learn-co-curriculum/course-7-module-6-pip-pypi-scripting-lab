from datetime import datetime
import os

def generate_log(data):
    # STEP 1: Validate input
    if not isinstance(data,list):
        raise ValueError("Input data must be a list")
    
    # Hint: Check if data is a list

    # STEP 2: Generate a filename with today's date (e.g., "log_20250408.txt")
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    # Hint: Use datetime.now().strftime("%Y%m%d")

    # STEP 3: Write the log entries to a file using File I/O
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")
    # Use a with open() block and write each line from the data list
    

    # STEP 4: Print a confirmation message with the filename
    print(f"Log written to {filename}")

    return filename