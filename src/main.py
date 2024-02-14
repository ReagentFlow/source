from fastapi import FastAPI
from src.config import DB_NAME
app = FastAPI()


@app.get("/")
async def root():
    return {"message": f"Hello World there is db named: {DB_NAME}"}