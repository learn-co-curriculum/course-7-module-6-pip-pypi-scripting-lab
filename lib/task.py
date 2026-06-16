class Task:
    def __init__(self, name):
        self.name = name
        self.completed = False  # starts as not done

    def mark_complete(self):
        self.completed = True

    def __repr__(self):
        status = "✅" if self.completed else "❌"
        return f"Task('{self.name}', completed={status})"