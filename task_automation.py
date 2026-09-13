import argparse
import os
from datetime import datetime
from rich.console import Console

console = Console()

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name: str):
        self.tasks.append({"task": task_name, "completed": False})
        console.print(f"[green]✔ Success:[/green] Added task: '[bold]{task_name}[/bold]'")

    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task["task"] == task_name:
                task["completed"] = True
                console.print(f"[green]✔ Success:[/green] Marked task '[bold]{task_name}[/bold]' as complete.")
                return
        console.print(f"[red]❌ Error:[/red] Task '{task_name}' not found.")

    def get_task_list(self):
        return [f"{'✅' if t['completed'] else '❌'} {t['task']}" for t in self.tasks]


def generate_log(data_list):
    if not isinstance(data_list, list):
        raise ValueError("Input must be of type list.")

    date_str = datetime.now().strftime("%Y%m%d")
    filename = f"log_{date_str}.txt"

    with open(filename, "w", encoding="utf-8") as file:
        for item in data_list:
            file.write(f"{item}\n")

    print(f"Confirmation: Log successfully created at {filename}")
    return filename


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automating Python Projects CLI Tool")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    add_parser = subparsers.add_parser("add-task", help="Add a new task")
    add_parser.add_argument("name", type=str, help="The name of the task to add")

    complete_parser = subparsers.add_parser("complete-task", help="Complete an existing task")
    complete_parser.add_argument("name", type=str, help="The name of the task to complete")

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