import os
import sys
from datetime import datetime
from lib.generate_log import generate_log

def fail(msg):
    print("FAIL:", msg)
    sys.exit(1)

# Test data
log_data = ["Entry one", "Entry two", "Entry three"]
filename = generate_log(log_data)

# Check file exists
if not os.path.exists(filename):
    fail(f"File {filename} was not created")

# Check filename format
today = datetime.now().strftime("%Y%m%d")
expected = f"log_{today}.txt"
if filename != expected:
    fail(f"Filename {filename} does not match expected {expected}")

# Check contents
with open(filename, 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f.readlines()]
if lines != log_data:
    fail("File contents do not match input data")

# Check invalid input raises
try:
    generate_log("not a list")
    fail("generate_log did not raise ValueError for invalid input")
except ValueError:
    pass

# Check empty list creates empty file
empty_filename = generate_log([])
with open(empty_filename, 'r', encoding='utf-8') as f:
    content = f.read()
if content != "":
    fail("Empty list did not create empty file")

os.remove(empty_filename)
# cleanup (remove unique files)
for f in {filename, empty_filename}:
    if os.path.exists(f):
        os.remove(f)

print("All checks passed")
sys.exit(0)
