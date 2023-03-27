import datetime
import pytest
from datetime import timedelta
from db.db import Base, Task
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


@pytest.fixture(scope="function")
def engine():
    engine = create_engine("sqlite:///test_db.sqlite")
    Base.metadata.create_all(bind=engine)
    yield engine
    Base.metadata.drop_all(bind=engine)
    engine.dispose()


@pytest.fixture(scope="function")
def session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()


@pytest.fixture(scope='function')
def today():
    return datetime.date.today()


@pytest.fixture(scope="function")
def tasks(session, today):
    tasks = [
        Task(title="task1", status="new", description="set up CI", deadline=today),
        Task(title="task2", status="new", description="finish the project", deadline=today + timedelta(days=1)),
        Task(title="task3", status="new", description="celebrate the success", deadline=today - timedelta(days=1)),
        Task(title="task4", status="in_progress", description="send code to review", deadline=today),
        Task(title="task5", status="in_progress", description="make adjustments", deadline=today + timedelta(days=1)),
        Task(title="task6", status="in_progress", description="test the functionality", deadline=today - timedelta(days=1)),
        Task(title="task7", status="done", description="set up mypy, flake8, pytest", deadline=today),
        Task(title="task8", status="done", description="write README.md", deadline=today),
    ]
    for task in tasks:
        session.add(task)
    session.commit()
    return tasks


def clear_db(session):
    session.query(Task).delete()
    session.commit()
