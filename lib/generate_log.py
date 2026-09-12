from datetime import datetime

def generate_log(log_data):
    """Writes log entries to a file and returns the filename."""
    if not isinstance(log_data, list):
        raise ValueError("Input must be a list")
        
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    
    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")
    
    print(f"Log file created: {filename}")
    
    return filename

if __name__ == "__main__":
    
    data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(data)
