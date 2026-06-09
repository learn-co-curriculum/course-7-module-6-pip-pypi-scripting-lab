from datetime import datetime


def generate_log(log_data):
    """
    Creates a timestamped log file and writes each log entry to it.
    """

    if not isinstance(log_data, list):
        raise ValueError("Input must be a list.")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")

    return filename