from datetime import datetime

def generate_log(log_data):
    # Validate input
    if not isinstance(log_data, list):
        raise ValueError("Input must be a list")

    # Create filename with today's date
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # Write data to file
    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    return filename