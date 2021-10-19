from fastapi import APIRouter
from tests.tenant.src.octoflow.tenants.tenant.settings import TenantSettings


def test_register_tenant_routes():
    settings = TenantSettings()
    assert isinstance(settings.routes, APIRouter)