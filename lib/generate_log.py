from datetime import datetime

def generate_log(log_data):
    """
    Generates a timestamped log file from a list of log entries.
    Raises ValueError if log_data is not a list.
    """
    if not isinstance(log_data, list):
        raise ValueError("Input data must be a list.")
    
    # Generate filename using the pattern log_YYYYMMDD.txt
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    
    # Write entries to the file (handles empty lists cleanly)
    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")
            
    # Print confirmation message including the filename
    print(f"Log written to {filename}")
    return filename

if __name__ == "__main__":
    # Sample data to execute when run from the command line
    sample_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(sample_data)