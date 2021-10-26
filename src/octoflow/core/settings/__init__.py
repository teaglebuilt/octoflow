from enum import Enum
from pathlib import Path
from typing import Optional, Dict
from pydantic import BaseSettings
from pydantic.main import BaseModel


class Loader(str, Enum):
    namespace = 'namespace'
    entrypoint = 'entrypoint'
    zip = 'zip'


class CoreSettings(BaseModel):
    tenants_home: Path
    loader: Loader

    class Config:
        use_enum_values = True

        
class Settings(BaseSettings):
    core: CoreSettings
    extensions: Optional[Dict]

    class Config:
        extra = 'allow'