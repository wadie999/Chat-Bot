from fastapi import FastAPI, Query
from .llm import run_query
from . import keys
import os




app = FastAPI()
os.environ["OPENAI_API_KEY"] = keys.key

@app.get("/query")
async def get_query_response(query: str = Query(..., description="Enter your query here")):
    response = run_query(query)
    return {"response": response}