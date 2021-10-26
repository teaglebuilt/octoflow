import sys
import pkgutil
from types import ModuleType
from contextlib import contextmanager
from importlib._bootstrap_external import SourceFileLoader

@contextmanager
def expand_sys_path(*paths: str):
    num = len(paths)
    for p in paths[::-1]:
        if p and isinstance(p, str):
            sys.path.insert(0, p)
    yield

    for _ in range(num):
        sys.path.pop(0)


def load_module_by_name(modname: str) -> ModuleType:
    loader: SourceFileLoader = pkgutil.get_loader(modname)
    return loader.load_module(modname)