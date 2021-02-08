class Task:
    def __init__(self, task):
        self.task = task

    def __str__(self):
        return self.task


print("Today:")
tasks = [Task("Do yoga"), Task("Make breakfast"), Task("Learn basics of SQL"), Task("Learn what is ORM")]
for i, task in enumerate(tasks):
    print(f"{i+1}) {task}")


if __name__ == "__main__":
    pass
