class Task:

    def __init__(self, title: str, description: str, status: str = "To Do"):
        self.title = title
        self.description = description
        self.__status = status  # how does it work?

    @property  # what is that?
    def status(self):
        return self.__status

    @status.setter  # what is that?
    def status(self, new_status: str):
        allowed_statuses = ["To Do", "In Progress", "Done"]
        if new_status in allowed_statuses:
            self.__status = new_status
        else:
            raise ValueError(
                f"ERROR, invalid status. There is only:{",".join(allowed_statuses)}"
            )  # how does it work?

    # beautiful task output
    def __str__(self):
        return f"{self.title} [{self.status}]"

    # For comparison
    def __eq__(self, other):
        return self.title == other.title and self.decription == other.description


class DailyTask:
    def __init__(self, name: str):
        self.name = name
        self.__tasks = []

    def add_task(self, task: Task):
        if not isinstance(task, Task):  # What is this
            raise TypeError("there is only Task objects!")  # what is this
        self.__tasks.append(task)

    @property
    def tasks(self):
        return self.__tasks.copy()

    def remove_task(self, task: Task):
        if task in self.__tasks:
            self.__tasks.remove(task)
        else:
            print(f"Task {task.title} is not defined")

    def show(self):
        print(f"\nProject: {self.name}")
        print("-" * 30)
        for i, task in enumerate(self.__tasks, 1):
            print(f"{i}. {task}")
        print("-" * 30)
