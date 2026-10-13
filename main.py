# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/welcome")
# def root():
#     return {"message": "Hello World"}

# @app.get("/welcome/{user}")
# def root(user: str):
#     return {"message": f"Hello welcome {user}"}

from fastapi import FastAPI

# create fastapi application
app = FastAPI()

@app.get("/") # Fast API to handle GET request to the root url
def home():
    return {"welcome home HARRYYY"}
