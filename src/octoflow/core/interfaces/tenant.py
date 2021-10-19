from importlib.metadata import EntryPoint
from typing import Callable, Tuple
from fastapi import FastAPI
from octoflow.models.tenant import Tenant


class TenantInterface:
    tenants: dict[str, Callable[..., Tenant]] = {}
    application: FastAPI = None

    @classmethod
    def init(cls, app: FastAPI):
        cls.application = app
        return app

    @classmethod
    def register(cls, tenant: str, fn: Callable[..., Tenant]):
        cls.tenants[tenant] = fn
        cls.application.include_router(
            cls.tenants[tenant].routes, prefix=f"/{tenant}")
        dags = cls.tenants[tenant].dags
        for dag_id, dag in dags.items():
            globals()[dag_id] = dag



def load_tenants(app: FastAPI, tenants: Tuple[EntryPoint] ) -> None:
    TenantInterface.init(app)
    for tenant in tenants:
        settings = tenant.load()
        registered_tenant = TenantInterface.register(
            tenant.name, settings())