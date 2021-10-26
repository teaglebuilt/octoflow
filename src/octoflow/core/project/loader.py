import sys
import pkgutil
import importlib
from importlib.metadata import entry_points
from pathlib import Path


global tenants
tenants = {}


def entrypoint_loader(tenants_home):
    for entrypoint in entry_points()[str(tenants_home)]:
        breakpoint()
        tenant = entrypoint.load()
        tenants[entrypoint.name] = tenant()
        return tenants


def namespace_loader(tenants_home):
    tenants = pkgutil.iter_modules(tenants_home.__path__, tenants_home.__name__, ".")


def zip_loader():
    pass


loaders = {
    "namespace": namespace_loader,
    "entrypoint": entrypoint_loader,
    "zip": zip_loader
}