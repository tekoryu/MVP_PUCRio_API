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
from schemas import *


# flask_openapi definitions
info = Info(title="PDF Leser", version="0.0.1")
app = OpenAPI(__name__, info=info)

# flask_openai tags
home_tag = Tag(name="Documentação",
               description="Seleção de documentação")
project_tag = Tag(name="Projeto",
                  description="Criação de um novo projeto, visualização e "
                  "remoção de um novo projeto.")
task_tag = Tag(name="Tarefa", description="Criação de uma nova tarefa, "
                                              "visualização e remoção de uma "
                                              "tarefa.")

@app.get("/", tags=[home_tag])
@cross_origin()
def home():
    """
    Redireciona para a tela de escolha de documentação de API
    """
    return redirect('/openapi')

"""
    PROJECT SECTION: METHODS AND ROUTES
"""

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
                       f"correspond to an item in DB.")
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

"""
    TASK SECTION: METHODS AND ROUTES
"""
@app.post("/task",
          tags=[task_tag],
          responses={"200": TaskViewSchema, "409": ErrorSchema, "400":
              ErrorSchema})
@cross_origin()
def add_task(form: TaskSchema):
    """
    Add a new task.

    Returns the recent added project.
    """
    project_id = form.project_id

    task = Task(
        name=form.name,
        description=form.description,
        header=form.header,
        footer=form.footer,
        line_overlap=form.line_overlap,
        line_margin=form.line_margin,
        char_margin=form.char_margin,
        page_numbers=form.page_numbers,
        resulting_text=form.resulting_text,
        tokenized_text=form.resulting_text,
    )
    print(task)
    logger.debug(f"Adding task {task.name} to the DB.")

    # creates a connection with the base
    session = Session()

    # find the parent project
    project= session.query(Project).filter(Project.id == project_id).first()

    # add new task and save changes
    project.add_task(task)
    session.commit()

    logger.debug(f"Task added to the project #{project_id}")

    return show_task(task)

@app.get('/tasks',
         tags=[task_tag],
         responses={"200": ListTaskSchema, "404": ErrorSchema })
@cross_origin()
def get_tasks():
    """
    Returns a list of tasks.
    """
    # busca na base as tarefas
    session = Session()
    tasks = session.query(Task).all()

    if not tasks:
        logger.debug("0 tasks found.")
        return {"tasks": []}, 200
    else:
        logger.debug(f"{len(tasks)} tasks found.")
        return list_tasks(tasks), 200

@app.get('/project_task',
         tags=[task_tag],
         responses={"200": ListTaskSchema, "404": ErrorSchema })
@cross_origin()
def get_tasks_by_project_id(query: TasksProjectSchema):
    """
    Returns a list of tasks by project id.
    """
    # busca na base as tarefas de um determinado projeto
    session = Session()
    project_id = query.project_id
    tasks = session.query(Task).filter(Task.project == project_id).all()

    if not tasks:
        logger.debug("0 tasks found.")
        return {"tasks": []}, 200
    else:
        logger.debug(f"{len(tasks)} tasks found.")
        return list_tasks(tasks), 200

@app.get('/task',
         tags=[task_tag],
         responses={"200": TaskViewSchema, "404": ErrorSchema})
@cross_origin()
def get_task(query: TaskSearchSchema):
    """
    Get task by name.
    """
    task_name = query.name
    logger.debug("Searching for task.")
    # recovers task data, if exists
    session = Session()
    project = session.query(Task).filter(Task.name ==
                                            task_name).first()

    if not task:
        error_msg = "Task not found. Consider recheck your spelling."
        logger.warning(f"Task not found. The name '{task_name}' do not "
                       f"correspond to an item in DB.")
        return {"message": error_msg}
    else:
        logger.debug(f"Task {task.name} found in the DB.")
        return show_task(task), 200

@app.delete('/delete/task',
            tags=[task_tag],
            responses={"200": TaskViewSchema, "404": ErrorSchema})
@cross_origin()
def delete_task(query: TaskSearchSchema):
    """
    Delete task.
    """
    task_name = unquote(unquote(query.name))
    logger.debug(f"Excluding task {task_name}")

    # performing item remotion
    session = Session()
    task_deleted = session.query(Task).filter(Task.name ==
                                           task_name).delete()
    session.commit()

    if task_deleted:
        logger.debug(f"The task was deleted.")
        return {"message": f"Task {task_name} was deleted from DB."}
    else:
        error_msg = "Task not found."
        logger.warning(f"The API was unable to perform the requested task "
                       f"exclusion.")
        return {"message": error_msg}, 404
