from typing import Optional
from fastapi import APIRouter
from airflow.models.dagbag import DagBag
import attr


@attr.s(auto_attribs=True)
class Settings:
    routes: Optional[APIRouter] = None
    dags: DagBag = None