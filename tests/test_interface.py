import tempfile
from airflow.configuration import get
from fastapi import testclient
from importlib.metadata import entry_points
import pytest

from octoflow.server.main import app


@pytest.fixture(scope="session")
def test_tenants(tmpdir_factory):
    fn = tmpdir_factory.mktemp("tenants")
    return fn


def test_load_tenants():
    for ep in entry_points()['octoflow.tenants']:
        breakpoint()
        tenant = ep.load()
        init_tenant = getattr(tenant, "init_tenant", None)