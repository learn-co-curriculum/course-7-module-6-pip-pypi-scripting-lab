import os

from datetime import datetime





def generate_log(data):

    # Step 1: validate input

    if not isinstance(data, list):

        raise ValueError("data must be a list")



    # Step 2: build the filename from today's date

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"



    # Step 3: write each entry on its own line

    with open(filename, "w") as file:

        for entry in data:

            file.write(f"{entry}\n")



    # Step 4: confirm and return the filename (the tests need the return value)

    print(f"Log written to {filename}")

    return filename