import tempfile
from fastapi import testclient
from fastapi.testclient import TestClient
import pytest

from octoflow.server.main import app


@pytest.fixture(scope="session")
def test_tenants(tmpdir_factory):
    fn = tmpdir_factory.mktemp("tenants")
    return fn


@pytest.fixture
def test_app(test_tenants):
    with TestClient(app) as test_app:
        yield test_app