"""
File: __init__.py
Author: Anderson Monteiro
Date: 04/12/2023
Description: Support file to call ORM and database oriented stuff.
"""
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from model.base import Base


db_path = "database"

# Verify if database folder exists. If not creates the folder.
if not os.path.exists(db_path):
    os.makedirs(db_path)

# Database url
db_url = 'sqlite:///%s/db.sqlite3' % db_path

# Creates database engine connection
engine = create_engine(db_url, echo=False)

# Instantiate the Session Factory
Session = sessionmaker(bind=engine)

# Verify if database exists, if note creates it
if not database_exists(engine.url):
    create_database(engine.url)

# Creates DB Structure
Base.metadata.create_all(engine)


