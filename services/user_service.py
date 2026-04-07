
from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def users():
    return {"users": ["Alice","Bob"]}
