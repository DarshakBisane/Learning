
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"Darshak Bisane's First API"}

@app.get("/Darshak Bisane")
def bisane():
    return {"Message" : "Something is Happening Crazy !"}

@app.get("/darshak/{id}")
def darshak(id:int):
    return {"user Id": id}