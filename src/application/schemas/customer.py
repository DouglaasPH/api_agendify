from pydantic import BaseModel

class CustomerInput (BaseModel):
    name: str
    email: str
