from datetime import datetime

def generate_log(log_data):
    """
    Creates a log file named log_YYYYMMDD.txt and writes the list items to it.
    """
    # Requirement: Raise ValueError if input is not a list
    if not isinstance(log_data, list):
        raise ValueError("Input must be a list of strings")
    
    # Requirement: Create filename with today's date
    today = datetime.now().strftime('%Y%m%d')
    filename = f"log_{today}.txt"
    
    # Requirement: Write each item on a new line
    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")
    
    # Requirement: Print confirmation message
    print(f"Log written to {filename}")
    
    return filename


# For running the file directly
if __name__ == "__main__":
    sample_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(sample_data)