import os

from db.database import create_database


def test_create_database() -> None:
    create_database()
    assert os.path.exists('tasks.db')
    assert os.path.exists('db/migrations')
