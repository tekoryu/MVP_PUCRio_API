"""
File: app.py
Author: Anderson Monteiro
Date: 04/12/2023
Description: First file called by flask. Contains routes and methods to
interact with the API.
"""
from flask import redirect
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from flask_openapi3 import OpenAPI, Info, Tag

from model.project import Project
from schemas import ProjectSchema, show_project, ProjectViewSchema, ErrorSchema


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
          responses={"200":ProjectViewSchema,
                     "409":ErrorSchema,
                     "400":ErrorSchema}
          )
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

    except IntegrityError as e:
        error_msg = "Já existe um projeto com esse nome."

    except Exception as e:
        # other errors
        error_msg = "Não foi possível salvar o projeto."
        return {"message": error_msg}, 400
