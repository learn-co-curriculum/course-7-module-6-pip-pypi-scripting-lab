from datetime import datetime
import os
import requests


def fetch_data():
  response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
  if response.status_code == 200:
    return response.json()
  return {}


def generate_log(data):
  # STEP 1: Validate input
  if not isinstance(data, list):
    print("Error: Input data must be a list.")
    return

  # STEP 2: Generate a filename with today's date
  filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

  # STEP 3: Write the log entries to a file using File I/O
  with open(filename, "w") as file:
    for entry in data:
      file.write(f"{entry}\n")

  # STEP 4: Print a confirmation message with the filename
  print(f"Log written to {filename}")


if __name__ == "__main__":
  # Fetch API post and create test data list
  post = fetch_data()
  title = post.get("title", "No title found")

  sample_data = [
      "User logged in",
      "User updated profile",
      f"Fetched Post Title: {title}",
      "Report exported",
  ]

  generate_log(sample_data)
