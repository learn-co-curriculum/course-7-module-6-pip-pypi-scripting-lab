#!/usr/bin/env python3
"""
Automation Tool: Task Manager
Demonstrates scripting, file I/O, and CLI patterns
"""

from datetime import datetime
import json
import os

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                return json.load(f)
        return []
    
    def save_tasks(self):
        with open(self.filename, "w") as f:
            json.dump(self.tasks, f, indent=2)
    
    def add_task(self, task_name):
        task = {
            "name": task_name,
            "completed": False,
            "created": datetime.now().isoformat()
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"✓ Task added: {task_name}")
    
    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            self.save_tasks()
            print(f"✓ Task completed: {self.tasks[task_index]['name']}")
        else:
            print("✗ Invalid task index")
    
    def list_tasks(self):
        if not self.tasks:
            print("No tasks found")
            return
        for i, task in enumerate(self.tasks):
            status = "✓" if task["completed"] else "○"
            print(f"{i}. {status} {task['name']}")

if __name__ == "__main__":
    import sys
    
    manager = TaskManager()
    
    if len(sys.argv) < 2:
        print("Usage: python automation_tool.py [add|complete|list] <task_name>")
        manager.list_tasks()
    elif sys.argv[1] == "add" and len(sys.argv) > 2:
        manager.add_task(" ".join(sys.argv[2:]))
    elif sys.argv[1] == "complete" and len(sys.argv) > 2:
        manager.complete_task(int(sys.argv[2]))
    elif sys.argv[1] == "list":
        manager.list_tasks()
    else:
        print("Invalid command")
