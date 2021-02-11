from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Table(Base):
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
    print("2) Add task")
    print("0) Exit")


def get_tasks():
    return session.query(Table).all()


def add_tasks(content):
    row = Table(task=content)
    session.add(row)
    session.commit()


if __name__ == "__main__":
    while True:
        menu()
        i = int(input())
        if i == 1:
            tasks = get_tasks()
            if tasks:
                for task in tasks:
                    print(task.task)
            else:
                print("Nothing to do!")
        elif i == 2:
            print("Enter task")
            add_tasks(input())
            print("The task has been added!")
        elif i == 0:
            print("Bye!")
            exit()
