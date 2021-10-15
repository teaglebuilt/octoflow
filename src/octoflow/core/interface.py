import importlib
from typing import Callable, List
from octoflow.models.tenant import Tenant

tenants: dict[str, Callable[..., Tenant]] = {}

def register(tenant: str, fn: Callable[..., Tenant]) -> None:
    tenants[tenant] = fn


class TenantInterface:

    def initialize() -> None:
        pass


def import_plugin(name: str) -> TenantInterface:
    return importlib.import_module(name)

def load_plugins(plugins: List[str]) -> None:
    for plugin_name in plugins:
        extension = import_plugin(plugin_name)
        extension.initialize()