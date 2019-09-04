"""How does the error response look like"""
from pydantic import BaseModel


class ErrorResponseModel(BaseModel): #pylint: disable=R0903
    """Error response model"""
    detail: str         # error message
