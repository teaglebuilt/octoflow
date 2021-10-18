from typing import Optional
from fastapi import APIRouter
import attr


@attr.s(auto_attribs=True)
class Settings:
    routes: Optional[APIRouter] = None