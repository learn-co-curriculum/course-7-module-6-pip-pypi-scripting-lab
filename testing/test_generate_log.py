import os
import pytest
from datetime import datetime
from lib.generate_log import generate_log 

def test_generate_log_creates_file():
    test_data = ["Error: Connection lost", "Info: Retry successful"]
    today_str = datetime.now().strftime("%Y%m%d")
    expected_filename = f"log_{today_str}.txt"
    
    # Act: Run your function
    result = generate_log(test_data)
    
    # Assert: Check that function returned the correct filename 
    assert result == expected_filename
    
    # Assert: Check that the physical file was actually created
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    full_file_path = os.path.join(root_dir, expected_filename)
    
    assert os.path.exists(full_file_path) == True
    
    # Clean up: Delete the test file after checking
    if os.path.exists(full_file_path):
        os.remove(full_file_path)

def test_generate_log_invalid_input():
    # Assert: Check if a ValueError is raised if input is not a list
    with pytest.raises(ValueError):
        generate_log("This is a string, not a list!")