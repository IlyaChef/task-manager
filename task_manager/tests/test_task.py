import argparse
import io
from datetime import datetime
from unittest.mock import patch

from _pytest.capture import CaptureFixture
from db.database import Task
from sqlalchemy.orm import Session
from task import show_tasks_deadline, create_task, show_tasks, move_task, show_in_progress


def test_create_task(session: Session) -> None:
    args = argparse.Namespace(
        title="Homework",
        description="Merge the homework",
        deadline="2023-04-01"
    )
    create_task(args, session)
    task = session.query(Task).filter_by(title="Homework").first()
    assert task is not None
    assert task.title == "Homework"
    assert task.description == "Merge the homework"
    assert task.deadline == datetime.strptime('2023-04-01', '%Y-%m-%d')


def test_show_tasks(capsys: CaptureFixture, session: Session, tasks: list[Task]) -> None:
    show_tasks([], session)
    output = capsys.readouterr().out.strip()

    for task in tasks:
        if task.status == "new":
            assert task.title in output
        else:
            assert task.title not in output


def test_show_in_progress(capsys: CaptureFixture, session: Session, tasks: list[Task]) -> None:
    show_in_progress([], session)
    output = capsys.readouterr().out.strip()

    for task in tasks:
        if task.status == "in_progress":
            assert task.title in output
        else:
            assert task.title not in output


def test_move_task(session: Session, tasks: list[Task], capsys: CaptureFixture) -> None:
    args = argparse.Namespace(task_id=1, status="in_progress")
    move_task(args, session)
    task = session.query(Task).filter_by(id=1).first()
    assert task.status == "in_progress"
    captured = capsys.readouterr()
    assert captured.out == f"Task 1 moved to {task.status}\n"


def test_show_tasks_deadline_today(session: Session, tasks: list[Task], today: datetime) -> None:
    test_input = today
    expected = [task.title for task in tasks if task.deadline == test_input]
    args = argparse.Namespace(date=test_input.strftime('%Y-%m-%d'))
    with patch('sys.stdout', new=io.StringIO()) as fake_output:
        show_tasks_deadline(args, session)
        output = fake_output.getvalue().strip()
        for task_title in expected:
            assert task_title in output
