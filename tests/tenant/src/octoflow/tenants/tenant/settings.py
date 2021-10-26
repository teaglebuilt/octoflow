import attr
from pathlib import Path
from airflow.models.dagbag import DagBag
from fastapi.routing import APIRouter
from octoflow.core.settings import Settings
from tests.tenant.src.octoflow.tenants.tenant.endpoints import routes


project_path = Path(__file__).expanduser().resolve().parent


@attr.s(auto_attribs=True)
class TenantSettings(Settings):
    routes: APIRouter = routes
    dags: DagBag = DagBag(project_path / "dags")