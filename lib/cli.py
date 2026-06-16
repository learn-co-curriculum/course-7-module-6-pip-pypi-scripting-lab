import argparse
from rich.console import Console
from user import User

console = Console()

# --- Global "database" (just a dict for now) ---
users = {}

def get_or_create_user(username):
    if username not in users:
        users[username] = User(username)
    return users[username]

def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI Tool")
    subparsers = parser.add_subparsers(dest="command")

    # --- add-task command ---
    add_parser = subparsers.add_parser("add-task", help="Add a task to a user")
    add_parser.add_argument("--user", required=True, help="Username")
    add_parser.add_argument("--task", required=True, help="Task name")

    # --- complete-task command ---
    complete_parser = subparsers.add_parser("complete-task", help="Mark a task as complete")
    complete_parser.add_argument("--user", required=True, help="Username")
    complete_parser.add_argument("--task", required=True, help="Task name")

    # --- show-tasks command (bonus!) ---
    show_parser = subparsers.add_parser("show-tasks", help="Show all tasks for a user")
    show_parser.add_argument("--user", required=True, help="Username")

    args = parser.parse_args()

    if args.command == "add-task":
        user = get_or_create_user(args.user)
        task = user.add_task(args.task)
        console.print(f"[green]✅ Task '[bold]{task.name}[/bold]' added for {user.username}![/green]")

    elif args.command == "complete-task":
        user = get_or_create_user(args.user)
        task = user.complete_task(args.task)
        if task:
            console.print(f"[blue]🎉 Task '[bold]{task.name}[/bold]' marked as complete![/blue]")
        else:
            console.print(f"[red]❌ Task '{args.task}' not found for {user.username}.[/red]")

    elif args.command == "show-tasks":
        user = get_or_create_user(args.user)
        user.display_tasks()

    else:
        parser.print_help()

if __name__ == "__main__":
    main()