"""
File: base.py
Author: Anderson Monteiro
Date: 04/12/2023
Description: Creates the Project model.
"""
from datetime import datetime

from model import Base
from sqlalchemy import Column, String, Integer, DateTime, Text

from model.task import Task


class Project(Base):
    """
    The model Project has identifying attributes, i.e name and description about
    the files that will be scanned down. Are they legislative initiatives?Are
    they books? Are they articles? That is the place.
    """
    __tablename__ = 'project'

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(255), unique=True)
    description = Column("description", Text)
    date_created = Column("date_created",
                          DateTime, default=datetime.now)

    def __init__(self, name: str, description: str):
        """
        Add new project

        :param name: str
            Project name. Unique. 255 chars.
        :param description: str
            Project description. No char limit.
        """
        self.name = name
        self.description = description

    def add_task(self, task: Task):
        """
        Add new task to the project

        :param task: Task object
        """
        pass