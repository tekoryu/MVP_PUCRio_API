"""
File: app.py
Author: Anderson Monteiro
Date: 04/12/2023
Description: First file called by flask. Contains routes and methods to
interact with the API.
"""

from flask import redirect
from sqlalchemy.exc import IntegrityError
from flask_openapi3 import OpenAPI, Info, Tag
from logger import logger

from model import Session, Project, Task
from schemas import ProjectSchema, show_project, ProjectViewSchema, ErrorSchema, ListProjectSchema


# flask_openapi definitions
info = Info(title="PDF Leser", version="0.0.1")
app = OpenAPI(__name__, info=info)

# flask_openai tags
home_tag = Tag(name="Documentação",
               description="Seleção de documentação")
project_tag = Tag(name="Projeto",
                  description="""Criação de um novo projeto, visualização
                   e remoção de um novo projeto.""")
task_project = Tag(name="Tarefa", description="")

@app.get("/", tags=[home_tag])
def home():
    """
    Redireciona para a tela de escolha de documentação de API
    """
    return redirect('/openapi')

@app.post("/project",
          tags=[project_tag],
          responses={"200": ProjectViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_project(form: ProjectSchema):
    """
    Add a new project to DB.

    Returns the recent added project.
    """
    project = Project(
        name=form.name,
        description=form.description,
    )

    logger.debug(f"Adding project {project.name} to the DB.")
    try:
        # creates a connection with the base
        session = Session()

        # add new project and save changes
        session.add(project)
        session.commit()
        logger.debug(f"Project {project.name} added with success!")
        return show_project(project), 200

    except IntegrityError as e:
        logger.warning(f"Unable to add project: {e}")
        error_msg = "Já existe um projeto com esse nome."
        return {"message": error_msg}, 409

    except Exception as e:
        # other errors
        error_msg = "Não foi possível salvar o projeto."
        logger.warning(f"Unable to add project: {Exception}")
        return {"message": error_msg}, 400

@app.get('/projects',
         tags=[project_tag],
         responses={"200": ListProjectSchema, "404": ErrorSchema })
def get_projects():
    """
    Returns a list of the projects
    """
    # busca na base os projetos
    session.Session()
    projects = session.query(Project).all()

    if not projects:
        logger.debug("0 projects found.")
        return {"projects": []}, 200
    else:
        logger.debug(f"{len(projects)} projects found.")
        return list_projects(projects), 200

@app.get('/produto',
         tags)


