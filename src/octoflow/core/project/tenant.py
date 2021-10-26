


from pydantic import BaseModel


class Tenant(BaseModel):
    pass

    class Config:
        arbitrary_types_allowed = True