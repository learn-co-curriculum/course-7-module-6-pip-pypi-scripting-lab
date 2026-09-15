import os
import argparse
from datetime import datetime
from task_manager.task_utils import TaskManager

def generate_log(data_list):
    # 1. Input Validation
    if not isinstance(data_list, list):
        raise ValueError("Input must be of type list.")
        
    # 2. Date and Filename Generation
    date_str = datetime.now().strftime("%Y%m%d")
    filename = f"log_{date_str}.txt"

    # 3. File Creation and Writing
    with open(filename, "w", encoding="utf-8") as file:
        for item in data_list:
            file.write(f"{item}\n")

    print(f"Confirmation: Log successfully created at {filename}")
    
    # 4. Critical Return Statement (Fixes the NoneType Error)
    return filename

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automating Python Tasks")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    add_parser = subparsers.add_parser("add-task", help="Add a new task")
    add_parser.add_argument("name", type=str, help="The name of the task")
    
    complete_parser = subparsers.add_parser("complete-task", help="Complete a task")
    complete_parser.add_argument("name", type=str, help="The name of the task")
    
    args = parser.parse_args()
    manager = TaskManager()
    
    # Starter mock data to generate log entries
    manager.add_task("Review project guidelines")
    manager.add_task("Configure virtual environment")
    
    if args.command == "add-task":
        manager.add_task(args.name)
    elif args.command == "complete-task":
        manager.complete_task(args.name)
        
    current_tasks = manager.get_task_list()
    generate_log(current_tasks)