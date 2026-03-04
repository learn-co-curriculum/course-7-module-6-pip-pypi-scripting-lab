import datetime
import os

def generate_log(log_entries):
    """
    Generate a log file with the given entries.
    
    Args:
        log_entries (list): List of log entry strings
        
    Returns:
        str: The filename of the created log file
        
    Raises:
        ValueError: If log_entries is not a list
    """
    # Check if input is a list
    if not isinstance(log_entries, list):
        raise ValueError("Input must be a list")
    
    # Generate filename with current date (YYYYMMDD format only)
    current_date = datetime.datetime.now().strftime("%Y%m%d")
    filename = f"log_{current_date}.txt"
    
    # Write entries to file (no header or footer)
    with open(filename, 'w') as file:
        for entry in log_entries:
            file.write(entry + '\n')
    
    # Print success message
    print(f"Success! Log written to: {filename}")
    print(f"File location: {os.path.abspath(filename)}")
    print(f"Number of entries: {len(log_entries)}")
    
    # Warning for empty list
    if len(log_entries) == 0:
        print("Warning: The list is empty. Creating empty log file.")
    
    return filename