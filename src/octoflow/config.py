from functools import lru_cache

from pathlib import Path
import toml
from octoflow.core.settings import Settings

current_dir = Path.cwd().expanduser().resolve()


class OctoflowConfig(Settings):
    pass


  
@lru_cache
def get_octoflow_settings():
    try:
        config = toml.load(current_dir / "octoflow.toml")
        return OctoflowConfig(**config)
    except FileNotFoundError:
        print("octoflow.cfg is required")


settings = get_octoflow_settings()