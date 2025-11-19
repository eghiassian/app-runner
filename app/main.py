from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI(title="My App Runner App", version="1.0.0")


@app.get("/")
def home():
    return {"message": "Hello from AWS App Runner! 🚀", "port": os.getenv("PORT")}


@app.get("/health")
def health():
    return {"status": "healthy"}


class Echo(BaseModel):
    text: str


@app.post("/echo")
def echo(body: Echo):
    return {"you_said": body.text}