import os

from task_manager.db.database import create_database


def test_create_database() -> None:
    create_database()
    assert os.path.exists('tasks.db')

