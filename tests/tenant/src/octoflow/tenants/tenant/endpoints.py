from fastapi import APIRouter


routes = APIRouter(tags=['tenant'])


@routes.get("/")
def index():
    print(f"hello from {__package__}")