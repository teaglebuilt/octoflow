from importlib.metadata import entry_points 
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.wsgi import WSGIMiddleware
from starlette.responses import JSONResponse
from airflow.www.app import create_app
from airflow.configuration import conf
from octoflow.core.interfaces.tenant import load_tenants

app = FastAPI()
app.mount("/airflow", WSGIMiddleware(create_app(config=conf)))


@app.on_event("startup")
def setup_application():
    tenants = entry_points()["octoflow.tenants"]
    if len(tenants) > 0:
        tenants = load_tenants(tenants, app)
        app.state.tenants = tenants


app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_origin_regex="https?://.*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", tags=["app"])
def healthcheck():
    return JSONResponse(content={"response": "all is good"})

