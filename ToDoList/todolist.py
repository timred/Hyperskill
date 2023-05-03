from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

today = datetime.today()


class Task(Base):
    # noinspection SpellCheckingInspection
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)


def menu():
    print("1) Today's tasks")
    print("2) Week's tasks")
    print("3) All tasks")
    print("4) Missed tasks")
    print("5) Add task")
    print("6) Delete task")
    print("0) Exit")


def get_tasks(datetime_day=None, missed=False):
    if not datetime_day and not missed:
        return session.query(Task).order_by(Task.deadline).all()
    elif missed:
        return session.query(Task).filter(Task.deadline < today.date()).order_by(Task.deadline).all()
    else:
        return session.query(Task).filter(Task.deadline == datetime_day.date()).all()


def add_tasks(content, deadline_time):
    row = Task(task=content, deadline=deadline_time)
    session.add(row)
    session.commit()


def delete_tasks(row):
    session.delete(row)
    session.commit()


def print_tasks(tasks, numbered=False, missed=False):
    if tasks and not numbered:
        for task in tasks:
            print(task.task)
    elif tasks and numbered:
        for task_number, task in enumerate(tasks):
            print(f"{task_number + 1}. {task.task}. {task.deadline.strftime('%d %b')}")
    elif missed:
        print("Nothing is missed!")
    else:
        print("Nothing to do!")
    print()


if __name__ == "__main__":
    while True:
        menu()
        choice = int(input())
        if choice == 1:
            print()
            print(f"Today {today.strftime('%d %b')}:")
            rows = get_tasks(today)
            print_tasks(rows)
        if choice == 2:
            for i in range(7):
                when = today + timedelta(days=i)
                rows = get_tasks(when)
                print()
                print(f"{when.strftime('%A %d %b')}:")
                print_tasks(rows)
        elif choice == 3:
            rows = get_tasks()
            print()
            print("All tasks:")
            print_tasks(rows, True)
        elif choice == 4:
            print()
            print("Missed tasks:")
            rows = get_tasks(missed=True)
            print_tasks(rows, numbered=True)
        elif choice == 5:
            print()
            print("Enter task")
            task_desc = input()
            print("Enter deadline")
            deadline = datetime.strptime(input(), "%Y-%m-%d")
            add_tasks(task_desc, deadline)
            print("The task has been added!")
            print()
        elif choice == 6:
            print()
            print("Choose the number of the task you want to delete:")
            rows = get_tasks()
            print_tasks(rows, numbered=True)
            print("Choose the number of the task you want to delete:")
            delete_tasks(rows[int(input())-1])
            print("The task has been deleted!")
        elif choice == 0:
            print("Bye!")
            exit()
