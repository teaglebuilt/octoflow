from fastapi import APIRouter
from airflow.models.dag import DAG
from airflow.models.dagbag import DagBag
from tests.tenant.src.octoflow.tenants.tenant import (
    settings, dags
)


def test_register_tenant_settings():
    tenant_settings = settings.TenantSettings()
    assert isinstance(tenant_settings.routes, APIRouter)
    assert isinstance(tenant_settings.dags, DagBag)

    def test_tenant_dags_registered():
        assert tenant_settings.dags.size() >= 1
        assert len(tenant_settings.dags.import_errors) == 0

    test_tenant_dags_registered()


def test_get_tenant_dag_from_dagbag():
    bag = DagBag(dag_folder=dags.__path__[0])
    dag = bag.get_dag('generate_dag')
    assert isinstance(dag, DAG)