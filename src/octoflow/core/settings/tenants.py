from pathlib import Path
from typing import Callable, Union
from pydantic import BaseModel
from octoflow.core.project.loader import (
  entrypoint_loader, namespace_loader, zip_loader
)


class Tenants(BaseModel):
    path: Path
    loader: str