"""
File: task.py
Author: Anderson Monteiro
Date: 10/12/2023
Description: Here we create Pydantic classes to control data types and type
hints in the application. The following schemas are task schemas, child
attributes of a project.
"""

from pydantic import BaseModel
from typing import List

from model.task import Task


class TaskSchema(BaseModel):
    """
    Defines how a task must be represented
    """
    project_id: int = 1
    name: str = "Avulso Inicial"
    description: str = ("Projeto de Lei do Senador Acácio que altera a Lei do "
                        "Genocídio")
    # page layout attributes
    header: int = 750
    footer: int = 70
    line_overlap: float = 0.5
    line_margin: float = 0.5
    char_margin: float = 2.0
    page_numbers: str = "1-25"
    pdf_file: str = "Lei do Aborto.pdf"
    resulting_text: str = "Here goes a really long text."
    tokenized_text: str = "Here goes a lot of words in list."


class TaskSearchSchema(BaseModel):
    name: str = "Substitutivo do Relator"


class ListTaskSchema(BaseModel):
    tasks: List[TaskSchema]


class TaskViewSchema(BaseModel):
    """
        Defines how a task will be represented
    """
    id: int = 1
    name: str = "Emendas propostas pelo governo"
    description: str = "Emendas Fazenda, MGI e SRI."


class TaskDeletionSchema(BaseModel):
    """
    Defines the data structure from the return message from a DELETE request.
    """
    message: str
    name: str


class TasksProjectSchema(BaseModel):
    """
    Project id.
    """
    project_id: int = 1


def show_task(task: Task):
    """
        Returns a representation of a task
    """
    return {
        "id": task.id,
        "name": task.name,
        "header": task.header,
        "footer": task.footer,
        "line_overlap": task.line_overlap,
        "line_margin": task.line_margin,
        "char_margin": task.char_margin,
        "page_numbers": task.page_numbers,
        "resulting_text": task.resulting_text,
        "tokenized_text": task.tokenized_text
    }


def list_tasks(tasks: List[Task]):
    result = []
    for task in tasks:
        result.append({
            "id": task.id,
            "name": task.name,
            "description": task.description,
            "date_created": task.date_added.strftime("%m/%d/%Y"),
        })
    return {"tasks": result}


# Define Pydantic model for file input
class FileInput(BaseModel):
    file: bytes
