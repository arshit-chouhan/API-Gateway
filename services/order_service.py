
from fastapi import FastAPI

app = FastAPI()

@app.get("/orders")
def orders():
    return {"orders": [101,102,103]}
