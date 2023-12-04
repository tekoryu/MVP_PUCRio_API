"""
File: base.py
Author: Anderson Monteiro
Date: 04/12/2023
Description: Creates the Task model.
"""
from datetime import datetime

from model import Base
from sqlalchemy import Column, Float, String, Integer, Text, DateTime


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
    header = Column("header", Float)
    footer = Column("footer", Float)
    line_overlap = Column("line_overlap", Float)
    line_margin = Column("line_margin", Float)
    char_margin = Column("char_margin", Float)
    page_numbers = Column("decodified_text", Text)
    resulting_text = Column("resulting_text", Text)
    tokenized_text = Column("tokenized_text", Text)

    def __init__(self,
                 name: str,
                 description: str,
                 header: float,
                 footer: float,
                 line_overlap: float,
                 line_margin: float,
                 char_margin: float,
                 page_numbers: float,
                 resulting_text: Text,
                 tokenized_text: Text,
                 ):
        self.name: name
        self.description: description
        self.header: header
        self.footer: footer
        self.line_overlap: line_overlap
        self.line_margin: line_margin
        self.char_margin: char_margin
        self.page_numbers: page_numbers
        self.resulting_text: resulting_text
        self.tokenized_text: tokenized_text
