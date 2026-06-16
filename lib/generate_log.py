from datetime import datetime
import os

def generate_log(data):
    if not isinstance(data, list):
        print("Error: data must be a list")
        return

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")

if __name__ == "__main__":
    log_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(log_data)
