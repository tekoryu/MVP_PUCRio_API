"""
File: base.py
Author: Anderson Monteiro
Date: 04/12/2023
Description: Model name Project, identities and attributes.
"""
from model import Base


class Project(Base):
    """
    Project stores attributes related to the project, i.e name, description and comments about the files that will be
    scanned down. Are they legislative projects? Are they books
    """