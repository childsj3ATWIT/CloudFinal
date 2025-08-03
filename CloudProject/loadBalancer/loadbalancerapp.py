import os

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    environment = os.getenv('APP_NAME', 'localhost')
    hello_message = f"Hello from FastAPI! Environment: {environment}"
    return {"message": hello_message}

@app.get("/hello")
async def hello(name: str, age: int):
    return {"name": name, "age": age}