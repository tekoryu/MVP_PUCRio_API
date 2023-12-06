"""
File: app.py
Author: Anderson Monteiro
Date: 04/12/2023
Description: First file called by flask. Contains routes and methods to
interact with the API.
"""
from flask import Flask

from model.project import Project

app = Flask(__name__)


@app.route("/")
def home():
    """
    Aqui vai entrar na tela da OPenAPI, quando houver.
    """
    return "Hello, world!"


@app.route("/project")
def add_project():
    """
    Add a new project to DB.

    Returns the recent added project.
    """
    project = Project(

    )
