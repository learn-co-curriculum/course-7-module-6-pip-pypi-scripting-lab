from task import Task

class User:
    def __init__(self, username):
        self.username = username
        self.tasks = []  # empty list to hold Task objects

    def add_task(self, task_name):
        task = Task(task_name)
        self.tasks.append(task)
        return task

    def complete_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.mark_complete()
                return task
        return None  # task wasn't found

    def display_tasks(self):
        if not self.tasks:
            print(f"{self.username} has no tasks yet.")
        else:
            print(f"\n📋 Tasks for {self.username}:")
            for task in self.tasks:
                status = "✅ Done" if task.completed else "❌ Pending"
                print(f"  - {task.name}: {status}")