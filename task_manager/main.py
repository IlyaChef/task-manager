import argparse
from sqlalchemy.orm import Session
from db.db import engine, create_database
from task import show_tasks, create_task, move_task, show_in_progress, show_tasks_deadline


def main() -> None:
    create_database()
    session = Session(bind=engine)

    parser = argparse.ArgumentParser(description='Task Manager')
    subparsers = parser.add_subparsers()

    parser_show = subparsers.add_parser('show', help='Show all new tasks to do')
    parser_show.set_defaults(func=lambda args: show_tasks(args, session))

    parser_show_in_progress = subparsers.add_parser('doing', help='Show all tasks in progress')
    parser_show_in_progress.set_defaults(func=lambda args: show_in_progress(args, session))

    parser_create = subparsers.add_parser('create', help='Add new task')
    parser_create.add_argument('--title', required=True, help='Task title')
    parser_create.add_argument('--description', required=True, help='Task description')
    parser_create.add_argument('--deadline', required=True, help='Task deadline')
    parser_create.set_defaults(func=lambda args: create_task(args, session))

    parser_move = subparsers.add_parser('move', help='Move task to another status')
    parser_move.add_argument('task_id', type=int, help='Task ID')
    parser_move.add_argument('status', choices=['new', 'in_progress', 'done'], help='Task status')
    parser_move.set_defaults(func=lambda args: move_task(args, session))

    parser_deadline = subparsers.add_parser('deadline', help='Show tasks with deadline before the specified date')
    parser_deadline.add_argument('date', help='Deadline date in format YYYY-MM-DD')
    parser_deadline.set_defaults(func=lambda args: show_tasks_deadline(args, session))

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
