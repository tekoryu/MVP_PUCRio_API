from pydantic import BaseModel


class ErrorSchema(BaseModel):
    """
    Defines the error message definiton
    """
    message: str
