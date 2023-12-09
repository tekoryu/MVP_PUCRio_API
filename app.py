"""
File: app.py
Author: Anderson Monteiro
Date: 04/12/2023
Description: First file called by flask. Contains routes and methods to
interact with the API.
"""

from flask import redirect
from flask_cors import CORS, cross_origin
from sqlalchemy.exc import IntegrityError
from flask_openapi3 import OpenAPI, Info, Tag
from logger import logger
from urllib.parse import unquote


from model import Session, Project, Task
from schemas import (ProjectSchema, show_project, ProjectViewSchema,
                     ErrorSchema, ListProjectSchema, ProjectSearchSchema,
                     list_projects)


# flask_openapi definitions
info = Info(title="PDF Leser", version="0.0.1")
app = OpenAPI(__name__, info=info)

# flask_openai tags
home_tag = Tag(name="Documentação",
               description="Seleção de documentação")
project_tag = Tag(name="Projeto",
                  description="Criação de um novo projeto, visualização e "
                  "remoção de um novo projeto.")
task_project = Tag(name="Tarefa", description="")

@app.get("/", tags=[home_tag])
@cross_origin()
def home():
    """
    Redireciona para a tela de escolha de documentação de API
    """
    return redirect('/openapi')

@app.post("/project",
          tags=[project_tag],
          responses={"200": ProjectViewSchema, "409": ErrorSchema, "400": ErrorSchema})
@cross_origin()
def add_project(form: ProjectSchema):
    """
    Add a new project.

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
@cross_origin()
def get_projects():
    """
    Returns a list of projects.
    """
    # busca na base os projetos
    session = Session()
    projects = session.query(Project).all()

    if not projects:
        logger.debug("0 projects found.")
        return {"projects": []}, 200
    else:
        logger.debug(f"{len(projects)} projects found.")
        return list_projects(projects), 200

@app.get('/project',
         tags=[project_tag],
         responses={"200": ProjectViewSchema, "404": ErrorSchema})
@cross_origin()
def get_project(query: ProjectSearchSchema):
    """
    Get project by id.
    """
    project_name = query.name
    logger.debug("Searching for project.")
    # recovers project data, if exists
    session = Session()
    project = session.query(Project).filter(Project.name ==
                                            project_name).first()

    if not project:
        error_msg = "Project not found. Consider recheck your spelling."
        logger.warning(f"Project not found. The name '{project_name}' do not "
                       f"correspond to a item in DB.")
        return {"message": error_msg}
    else:
        logger.debug(f"Project {project.name} found in the DB.")
        return show_project(project), 200

@app.delete('/delete/project',
            tags=[project_tag],
            responses={"200": ProjectViewSchema, "404": ErrorSchema})
@cross_origin()
def delete_project(query: ProjectSearchSchema):
    """
    Delete project.
    """
    project_name = unquote(unquote(query.name))
    logger.debug(f"Excluding project {project_name}")

    # performing item remotion
    session = Session()
    project_deleted = session.query(Project).filter(Project.name ==
                                           project_name).delete()
    session.commit()

    if project_deleted:
        logger.debug(f"The project was deleted.")
        return {"message": f"Project {project_name} was deleted from DB."}
    else:
        error_msg = "Project not found."
        logger.warning(f"The API was unable to perform the requested project "
                       f"exclusion.")
        return {"message": error_msg}, 404
