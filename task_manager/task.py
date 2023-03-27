import argparse
from datetime import datetime

from sqlalchemy.orm import Session

from db.database import Task


def show_tasks(args: argparse.Namespace, session: Session) -> None:
    tasks = session.query(Task).filter_by(status='new').all()
    for task in tasks:
        deadline_str = f"deadline: {task.deadline.strftime('%Y-%m-%d')}"
        status_str = f"status: {task.status}"
        description_str = f" *** description: {task.description}" if task.description else ""

        print(f"{task.id}. {task.title} - {status_str} ({deadline_str}) {description_str}")


def create_task(args: argparse.Namespace, session: Session) -> None:
    deadline = datetime.strptime(args.deadline, '%Y-%m-%d').date()
    task = Task(title=args.title, description=args.description, deadline=deadline)
    session.add(task)
    session.commit()
    print(f"Task {task.id} created")


def move_task(args: argparse.Namespace, session: Session) -> None:
    task = session.query(Task).filter_by(id=args.task_id).first()
    if not task:
        raise argparse.ArgumentTypeError(f"No task with id {args.task_id}")
    task.status = args.status
    session.commit()
    print(f"Task {task.id} moved to {task.status}")


def show_in_progress(args: argparse.Namespace, session: Session) -> None:
    tasks = session.query(Task).filter_by(status='in_progress').all()
    for task in tasks:
        deadline_str = f"deadline: {task.deadline.strftime('%Y-%m-%d')}"
        status_str = f"status: {task.status}"
        description_str = f" *** description: {task.description}" if task.description else ""

        print(f"{task.id}. {task.title} - {status_str} ({deadline_str}) {description_str}")


def show_tasks_deadline(args: argparse.Namespace, session: Session) -> None:
    deadline = datetime.strptime(args.date, '%Y-%m-%d').date()
    tasks = session.query(Task).filter(Task.deadline <= deadline).all()
    for task in tasks:
        deadline_str = f"deadline: {task.deadline.strftime('%Y-%m-%d')}"
        status_str = f"status: {task.status}"
        description_str = f" *** description: {task.description}" if task.description else ""

        print(f"{task.id}. {task.title} - {status_str} ({deadline_str}) {description_str}")
