from datetime import datetime

# Log entries
log_data = [
    "User logged in",
    "User updated profile",
    "Report exported"
]

# Generate a filename using today's date
filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

# Write the log entries to the file
with open(filename, "w") as file:
    for entry in log_data:
        file.write(f"{entry}\n")

# Display confirmation
print(f"Log written to {filename}")
