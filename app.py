"""
File: app.py
Author: Anderson Monteiro
Date: 04/12/2023
Description: First file called by flask. Contains routes and methods to
interact with the API.
"""
from flask import Flask
from sqlalchemy.orm import Session

from model.project import Project
from schemas import ProjectSchema, show_project

app = Flask(__name__)


@app.route("/")
def home():
    """
    Aqui vai entrar na tela da OPenAPI, quando houver.
    """
    return "Hello, world!"


@app.post("/project")
def add_project(form: ProjectSchema):
    """
    Add a new project to DB.

    Returns the recent added project.
    """
    project = Project(
        name=form.name,
        description=form.description,
    )

    try:
        # creates a connection with the base
        session = Session()

        # add new project and save changes
        session.add(project)
        session.commit()
        return show_project(project), 200

    except integrityError as e:
        error_msg = "Já existe um projeto com esse nome."

    except Exception as e:
        # other errors
        error_msg = "Não foi possível salvar o projeto."
        return {"message": error_msg}, 400



