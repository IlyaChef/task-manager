import os
from db.db import create_database


def test_create_database():
    create_database()
    assert os.path.exists('tasks.db')
    assert os.path.exists('db/migrations')
