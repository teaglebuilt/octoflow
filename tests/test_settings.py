import attr
from importlib.metadata import entry_points
from octoflow.core.settings import Settings
from fastapi import APIRouter


@attr.s(auto_attribs=True)
class TenantSettings(Settings):
    routes = APIRouter()


def test_register_tenant_routes():
    settings = TenantSettings()
    assert isinstance(settings.routes, APIRouter)