from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"Hello": "World"}


@app.get("/register")
def register():
    pass

@app.get("/signin")
def signin():
    pass

