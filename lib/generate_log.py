from datetime import datetime

def generate_log(log_data):

    # 1. validate input
    if not isinstance(log_data, list):
        raise ValueError("Input must be a list")

    # 2. create filename (MUST match test format)
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # 3. write file (even empty list must create file)
    with open(filename, "w") as file:
        for item in log_data:
            file.write(f"{item}\n")

    # 4. print confirmation (test expects this behavior)
    print(f"Log written to {filename}")

    # 5. CRITICAL: return filename (this fixes ALL your errors)
    return filename