from datetime import datetime
import os


def generate_log(log_data):
    """
    Creates a timestamped log file and writes log entries into it.
    """

    if not isinstance(log_data, list):
        raise ValueError("log_data must be a list")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")

    return filename


if __name__ == "__main__":
    logs = [
        "User logged in",
        "User updated profile",
        "Report exported"
    ]

    generate_log(logs)
