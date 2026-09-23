import sys
import datetime
import requests

def generate_log():
    # Format today's date as YYYYMMDD
    date_str = datetime.datetime.now().strftime("%Y%m%d")
    filename = f"log_{date_str}.txt"
    
    try:
        with open(filename, "w") as file:
            file.write(f"Log generated on {date_str}\n")
        print(f"Successfully created log file: {filename}")
        return filename
    except IOError as e:
        print(f"File writing error: {e}")
        return None

def fetch_data():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def save_output(data, filename="output.txt"):
    try:
        with open(filename, "w") as file:
            file.write(f"Automation Output Results:\n{data}\n")
        print(f"Successfully saved results to {filename}")
    except IOError as e:
        print(f"File writing error: {e}")

def main():
    print("Executing automation script...")
    generate_log()
    data = fetch_data()
    if data:
        print("Fetched Data:", data)
        save_output(data)

if __name__ == "__main__":
    main()