from datetime import datetime


def generate_log(log_data):
    """
    Creates a log file and writes each entry to it.
    Returns the filename.
    """

    if not isinstance(log_data, list):
        raise ValueError("log_data must be a list")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    return filename