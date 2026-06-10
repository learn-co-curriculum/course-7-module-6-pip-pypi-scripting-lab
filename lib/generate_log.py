# generate_log.py
# Automation tool that generates a timestamped log file from a list of entries.

from datetime import datetime


def generate_log(entries):
    """
    Generates a timestamped log file from a list of log entries.
    
    Args:
        entries (list): A list of log entry strings.
    
    Returns:
        str: The filename of the created log file.
    
    Raises:
        ValueError: If entries is not a list.
    """
    # Validate input - must be a list
    if not isinstance(entries, list):
        raise ValueError("entries must be a list")

    # Create filename with today's date
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # Write entries to file
    with open(filename, "w") as file:
        for entry in entries:
            file.write(f"{entry}\n")

    # Print confirmation message
    print(f"Log written to {filename}")

    return filename


if __name__ == "__main__":
    log_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(log_data)
