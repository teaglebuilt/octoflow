from typing import Dict, Type
from pathlib import Path
from pydantic import BaseModel
import toml
from octoflow.core.project.loader import loaders
from octoflow.core.settings import Settings

current_dir = Path.cwd().expanduser().resolve()
config = toml.load(current_dir / "octoflow.toml")

Project = Type['Project']


class Project(BaseModel):
    path: Path = current_dir
    settings: Settings = Settings(**toml.load(path / "octoflow.toml"))

    def load(self) -> Project:
        return loaders[
          self.settings.tenants.loader](
            self.settings.tenants.path
          )