import os
import sys
import inspect
import importlib
from typing import Callable, List
from fastapi import FastAPI, APIRouter

from octoflow.models.tenant import Tenant

tenants: dict[str, Callable[..., Tenant]] = {}

def register(tenant: str, fn: Callable[..., Tenant]) -> None:
    tenants[tenant] = fn


class TenantInterface:

    @staticmethod
    def initialize() -> None:
        pass


def import_routes(tenant) -> APIRouter:
    return importlib.import_module(f"{tenant.group}.{tenant.name}.routes")


def load_tenants(app: FastAPI, tenants: List[str]) -> None:
    for tenant in tenants:
        routes = import_routes(tenant)
        app.include_router(routes.routes, prefix=f"/{tenant.name}")