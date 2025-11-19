from datetime import datetime
import requests


class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def complete(self):
        self.completed = True

    def __repr__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.description}"


class User:
    def __init__(self, username):
        self.username = username
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_task(self, description):
        for task in self.tasks:
            if task.description == description:
                return task
        return None


class TaskManager:
    def __init__(self):
        self.users = {}

    def get_user(self, username):
        if username not in self.users:
            self.users[username] = User(username)
        return self.users[username]

    def add_task(self, username, description):
        user = self.get_user(username)
        task = Task(description)
        user.add_task(task)
        return task

    def complete_task(self, username, description):
        user = self.get_user(username)
        task = user.get_task(description)
        if task:
            task.complete()
        return task

    def list_tasks(self, username):
        user = self.get_user(username)
        return user.tasks


def generate_log(data):
    """Write log entries to a dated file."""
    if not isinstance(data, list):
        raise ValueError("Data must be a list")
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")
    print(f"Log written to {filename}")
    return filename


def fetch_api_data():
    """Fetch a post title from a public API."""
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        response.raise_for_status()
        post = response.json()
        return f"Fetched Post Title: {post.get('title', 'No title found')}"
    except requests.RequestException as e:
        return f"API fetch failed: {e}"


if __name__ == "__main__":
    # Example usage
    manager = TaskManager()
    manager.add_task("Manuel", "Write automation script")
    manager.add_task("Manuel", "Test API fetch")
    manager.complete_task("Manuel", "Write automation script")

    # Create log entries from tasks
    logs = [str(task) for task in manager.list_tasks("Manuel")]

    # Add API fetch log
    logs.append(fetch_api_data())

    # Write to file
    generate_log(logs)
