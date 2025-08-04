from pydantic import BaseModel, Field

class VirtualMachine(BaseModel):
    name: str
    ram: float
    cpu: float 
    storage: float
    os: str 
