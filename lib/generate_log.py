from datetime import datetime
import os

def generate_log(data):
    # STEP 1: Validate input - check if data is a list
    if not isinstance(data, list):
        raise ValueError("data must be a list.")

    # STEP 2: Generate a filename with today's date (e.g., "log_20250408.txt")
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # STEP 3: Write the log entries to a file using File I/O
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: Print a confirmation message with the filename and return it
    print(f"Log written to {filename}")
    return filename


if __name__ == "__main__":
    log_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(log_data)