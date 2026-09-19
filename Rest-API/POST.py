from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.post("/")
def hello():
    return("Hallo bhaiya ji")

class User(BaseModel):
    id : int
    name : str

@app.post("/user")
def userData(user: User):
    return{"message" : "User Data",
           "Data" : user}