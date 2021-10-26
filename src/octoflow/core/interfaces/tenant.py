import pkgutil
import importlib
import shutil
from importlib.metadata import EntryPoint
from types import ModuleType
from typing import Callable, Tuple
from fastapi import FastAPI
from airflow.utils.session import provide_session
from octoflow.models.tenant import Tenant
import octoflow
from octoflow.utils import expand_sys_path

class TenantInterface:
    tenants: dict[str, Callable[..., Tenant]] = {}
    application: FastAPI = None

    @classmethod
    def register(cls, 
        tenant: str, 
        fn: Callable[..., Tenant],
        app: FastAPI = None
    ):
        cls.tenants[tenant] = fn
        if app:
            cls.application = app
            cls.application.include_router(
                cls.tenants[tenant].routes, prefix=f"/{tenant}")
        if cls.tenants[tenant].dagbag:
            cls.register_to_airflow(cls.tenants[tenant])
        return cls.tenants

    @staticmethod
    @provide_session
    def register_to_airflow(tenant, session=None):
        for dag_id, dag in tenant.dagbag.dags.items():
            globals()[dag_id] = dag
            tenant.dagbag.sync_to_db()

    
def load_tenant_entries(tenants: Tuple[EntryPoint], app: FastAPI = None) -> None:
    for tenant in tenants:
        settings = tenant.load()
        registered_tenant = TenantInterface.register(
            tenant.name, settings(), app)
    return TenantInterface.tenants


def iter_namespace(ns_pkg):
    return pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__, + ".")


def load_tenants_namespace():
    tenants = {
        importlib.import_module(module_name)
        for _, module_name, _ in 
        iter_namespace(octoflow.tenants)
    }
    return tenants