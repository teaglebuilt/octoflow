from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.wsgi import WSGIMiddleware
from starlette.responses import JSONResponse
from airflow.www.app import create_app


app = FastAPI()
app.mount("/airflow", WSGIMiddleware(create_app()))


app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_origin_regex="https?://.*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.get("/health")
def healthcheck():
    return JSONResponse(content={"response": "all is good"})

