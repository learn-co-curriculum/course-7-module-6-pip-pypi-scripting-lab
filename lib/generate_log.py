from datetime import datetime

def generate_log(data):
    if not isinstance(data, list):
        raise ValueError("data must be a list")

    today = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today}.txt"

    with open(filename, 'w') as f:
        for entry in data:
            f.write(f"{entry}\n")

    print(f"Log generated: {filename}")
    return filename

if __name__ == "__main__":
    generate_log(["System start", "User login"])
    # TODO: Implement log generation logic

    # STEP 1: Validate input
    # Hint: Check if data is a list

    # STEP 2: Generate a filename with today's date (e.g., "log_20250408.txt")
    # Hint: Use datetime.now().strftime("%Y%m%d")

    # STEP 3: Write the log entries to a file using File I/O
    # Use a with open() block and write each line from the data list
    # Example: file.write(f"{entry}\n")

    # STEP 4: Print a confirmation message with the filename

    pass
