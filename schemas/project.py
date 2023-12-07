"""
File: project.py
Author: Anderson Monteiro
Date: 06/12/2023
Description: Here we create Pydantic classes to control data types and type hints in the application. I am not sure of
how this will be usefull in Django apps, but I'll give it a try. A colleague mentioned the use of the Marshmallow
library as a substitute. I'll try it in the next project.
"""
import datetime

from pydantic import BaseModel
from typing import List

from model.project import Project


class ProjectSchema(BaseModel):
    """
        Defines how a project must be represented.
    """

    name: str = "Projetos de Lei"
    description: str = "Projetos de Lei com tramitação no Senado Federal, avulso obtido através da página " \
                       "de acompanhamento"


class ProjectSearchSchema(BaseModel):
    """
        Defines how a project must be searched.
    """
    name: str = "Legislação"


class ListProjectSchema(BaseModel):
    """
        Defines how a list of projects must be represented.
    """
    projects: List[ProjectSchema]


class ProjectViewSchema(BaseModel):
    """
        Defines how a project will be represented.
    """
    id: int = 1
    name: str = "Projetos de Lei"
    description: str = "Projetos de Lei com tramitação no Senado"
    date_created: datetime.date = "01/04/2023"


class ProjectDeletionSchema(BaseModel):
    """
        Defines the data structure from the return message from a DELETE request
    """
    message: str
    name: str


def show_project(project: Project):
    """
        Returns a representation of the projects, using the ProjectViewSchema
    """
    return {
        "id": project.id,
        "name": project.name,
        "description": project.description,
        "date_created": project.date_created,
    }


def list_projects(projects: List[Project]):
    """
        Return a representation of the projects, using ProjectViewSchema
    """
    result = []
    for project in projects:
        result.append({
            "name": project.nome,
            "description": project.description,
        })
