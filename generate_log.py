from lib.generate_log import generate_log

log_data = ["User logged in", "User updated profile", "Report exported"]

if __name__ == "__main__":
    # Call the already-tested function from lib/generate_log.py
    filename = generate_log(log_data)
    print(f"File '{filename}' successfully created!")