import attr
from fastapi.routing import APIRouter
from octoflow.core.settings import Settings
from tests.tenant.src.octoflow.tenants.tenant.endpoints import routes


@attr.s(auto_attribs=True)
class TenantSettings(Settings):
    routes: APIRouter = routes