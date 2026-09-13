from datetime import datetime


def generate_log(data):
    # STEP 1: Validate input
    if not isinstance(data, list):
        raise ValueError("Data must be a list")

    # STEP 2: Generate a filename with today's date
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # STEP 3: Write the log entries to the file
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: Print a confirmation message
    print(f"Log written to {filename}")

    # Return the filename
    return filename