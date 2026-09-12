from datetime import datetime


def generate_log(log_data):
    if not isinstance(log_data, list):
        raise ValueError("Input must be a list")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    return filename


if __name__ == "__main__":
    sample_logs = [
        "User logged in",
        "User updated profile",
        "Report exported"
    ]

    filename = generate_log(sample_logs)
    print(f"Log written to {filename}")

