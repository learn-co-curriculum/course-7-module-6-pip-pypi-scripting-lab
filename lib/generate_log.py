from datetime import datetime
import os


def generate_log(log_entries, output_dir="."):
    if not isinstance(log_entries, list):
        raise ValueError("log_entries must be a list.")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, "w") as file:
        for entry in log_entries:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")
    return filename


if __name__ == "__main__":
    sample_logs = [
        "User logged in",
        "User updated profile",
        "Report exported",
    ]
    generate_log(sample_logs)