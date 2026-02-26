from datetime import datetime

def generate_log(log_entries):
    if not isinstance(log_entries, list):
        raise ValueError("log_entries must be a list")

    today = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today}.txt"

    with open(filename, "w") as file:
        for entry in log_entries:
            file.write(f"{entry}\n")

    return filename