import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from lib.generate_log import generate_log
from datetime import datetime

def test_generate_log():
    # Test 1: Valid input
    print("Test 1: Valid log data...")
    log_entries = ["Entry 1", "Entry 2", "Entry 3"]
    filename = generate_log(log_entries)
    expected = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    
    assert filename == expected, "Filename pattern wrong"
    assert os.path.exists(filename), "File not created"
    
    with open(filename, 'r') as f:
        content = f.read().strip().split('\n')
    assert content == log_entries, "Content mismatch"
    os.remove(filename)
    print("✓ Passed")
    
    # Test 2: Empty list
    print("Test 2: Empty list...")
    filename = generate_log([])
    assert os.path.exists(filename), "File not created"
    with open(filename, 'r') as f:
        assert f.read() == "", "Should be empty"
    os.remove(filename)
    print("✓ Passed")
    
    # Test 3: Invalid input
    print("Test 3: Invalid input (should raise ValueError)...")
    try:
        generate_log("not a list")
        print("✗ Failed - should have raised ValueError")
    except ValueError:
        print("✓ Passed")
    
    print("\n✅ All tests passed!")

if __name__ == "__main__":
    test_generate_log()
