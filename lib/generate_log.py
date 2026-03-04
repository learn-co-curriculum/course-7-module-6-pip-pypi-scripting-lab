from datetime import datetime
from pathlib import Path

def generate_log(log_entries):
    """
    Create a timestamped log file from a list of log entry strings.

    - Filename pattern: log_YYYYMMDD.txt
    - Writes each entry on its own line
    - Raises ValueError if log_entries is not a list
    - Supports empty lists (creates an empty log file)
    - Prints a confirmation message including the filename
    """
    # Validate input type
    if not isinstance(log_entries, list):
        raise ValueError("log_entries must be a list")

    # Build timestamped filename
    today_str = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today_str}.txt"
    filepath = Path(filename)

    # Write entries
    with filepath.open("w", encoding="utf-8") as file:
        for entry in log_entries:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")
    return filename


if __name__ == "__main__":
    sample_entries = ["User logged in", "User updated profile", "Report exported"]
    generate_log(sample_entries)
