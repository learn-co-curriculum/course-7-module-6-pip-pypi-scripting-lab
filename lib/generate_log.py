from datetime import datetime
import os

def generate_log(data):
    # STEP 1: Validate input
    if not isinstance(data, list):
        raise ValueError("Data must be a list of log entries")

    # STEP 2: Generate a filename with today's date
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # STEP 3: Write the log entries to a file
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: Print a confirmation message
    print(f"Log written to {filename}")

    # Return the filename for tests or cleanup
    return filename


if __name__ == "__main__":
    log_entries = ["User logged in", "User updated profile", "Report exported"]
    file_created = generate_log(log_entries)


    if os.path.exists(file_created):
        os.remove(file_created)
        print(f"Log file {file_created} removed after execution")
