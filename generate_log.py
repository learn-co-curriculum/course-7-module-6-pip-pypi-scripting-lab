from datetime import datetime

def write_log():
    log_data = ["User logged in", "User updated profile", "Report exported"]

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")


if __name__ == "__main__":
    write_log()