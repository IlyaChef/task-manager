import os
from alembic.config import Config
from alembic import command
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from typing import Type

Base: Type = declarative_base()
engine = create_engine('sqlite:///tasks.db')
Session = sessionmaker(bind=engine)


class Task(Base):
    __tablename__ = 'Tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    status = Column(String, default='new')
    deadline = Column(DateTime)


def create_database() -> None:
    if not os.path.exists('tasks.db'):
        Base.metadata.create_all(engine)
        alembic_cfg = Config('alembic.ini')
        alembic_cfg.set_main_option('script_location', 'db/migrations')
        command.revision(alembic_cfg, autogenerate=True, message='Init')
        command.upgrade(alembic_cfg, 'head')


if __name__ == '__main__':
    create_database()
