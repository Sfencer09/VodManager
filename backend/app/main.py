from fastapi import FastAPI

app = FastAPI()


@app.get("/echo")
def echo():
    return {"status": "OK"}