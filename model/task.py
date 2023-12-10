"""
File: task.py
Author: Anderson Monteiro
Date: 04/12/2023
Description: Creates the Task model.
"""
from datetime import datetime

from model import Base
from sqlalchemy import Column, Float, String, Integer, Text, DateTime, \
    ForeignKey


class Task(Base):
    """
    Tasks are the set of attributes that generates a compiled text. PDF files,
    page layouts, paragraph attributes, page ranges. Most of them are optional
    but don't be scared! Playing with levers and gears possibily will make
    your resulting text more coese!
    """
    __tablename__ = 'task'

    # identity attributes
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(255), default="Sem Nome")
    description = Column("descritption", String(255))
    date_added = Column("date_added", DateTime, default=datetime.now)

    # page layout attributes
    header = Column("header", Integer)
    footer = Column("footer", Integer)
    line_overlap = Column("line_overlap", Float)
    line_margin = Column("line_margin", Float)
    char_margin = Column("char_margin", Float)
    page_numbers = Column("page_numbers", String)
    resulting_text = Column("resulting_text", Text)
    tokenized_text = Column("tokenized_text", Text)

    # relacionamento, a ideia aqui é semelhante a do Django
    project = Column(Integer, ForeignKey("project.id"), nullable=False)