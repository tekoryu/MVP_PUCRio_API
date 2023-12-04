"""
File: base.py
Author: Anderson Monteiro
Date: 04/12/2023
Description: Model name Project, identities and attributes.
"""
from datetime import datetime

from model import Base
from sqlalchemy import Column, String, Integer, DateTime, Float, Text


class Project(Base):
    """
    Project stores attributes related to the project, i.e name, description and comments about the files that will be
    scanned down. Are they legislative projects? Are they books? Are they articles? That is the place.
    """
    __tablename__ = 'project'

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(255), unique=True)
    description = Column("description", Text)
    date_created = Column("date_created", default=datetime.now)

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

    def add_task(self, task:Task):
        """
        Add new task to the project

        :param task: Task object
        """
        pass