from pydantic import BaseModel
from datetime import datetime


class BaseSchema(BaseModel):
    class Config:
        orm_mode = True



class errorMessage(BaseModel):
    message: str



class ValidatorError(BaseModel):
    message: str = "Invalid Content"

