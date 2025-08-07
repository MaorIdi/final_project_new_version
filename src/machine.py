from pydantic import BaseModel, Field


class VirtualMachine(BaseModel):
    name: str = Field(..., example="new-vm")
    memory: float = Field(..., gt=0, example=2.0)
    cpu: float = Field(..., gt=0, example=2.0)
    storage: float = Field(..., gt=0, example=30.0)
    os: str = Field(
        ...,
        example="Linux",
        pattern="^(w|win|windows|lin|l|linux)$",
    )
