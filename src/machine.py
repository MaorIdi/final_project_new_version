from pydantic import BaseModel, Field


class VirtualMachine(BaseModel):
    name: str = Field(min_length=1, strip_whitespace=True)
    ram: float = Field(gt=0)
    cpu: float = Field(gt=0)
    storage: float = Field(gt=0)
    os: str = Field(pattern=r"^(windows|linux|win|lin|w|l)$")
