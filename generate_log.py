from datetime import datetime

def generate_log(log_data):
    if not isinstance(log_data, list):
        raise ValueError("log_data must be a list")
    
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    
    with open(filename, "w", encoding="utf-8") as f:
        for item in log_data:
            f.write(f"{item}\n")
            
    return filename

if __name__ == "__main__":
    sample_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(sample_data)