from fastapi import FastAPI, Query
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from .llm import run_query
from . import keys
import os

app = FastAPI()
os.environ["OPENAI_API_KEY"] = keys.key

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_root():
    return FileResponse('static/index.html')

@app.get("/query")
async def get_query_response(query: str = Query(..., description="Enter your query here")):
    response = run_query(query)
    return {"response": response}
