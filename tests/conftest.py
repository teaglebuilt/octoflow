import platform
import multiprocessing
from fastapi.testclient import TestClient
from octoflow.server.main import app


def pytest_configure(config):
    if platform in ["darwin", "windows"]:
        multiprocessing.set_start_method("spawn")
    else:
        multiprocessing.set_start_method("fork")


def octoflow_server():
    with TestClient(app) as server:
        yield server