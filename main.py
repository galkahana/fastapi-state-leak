from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def hello(request: Request):
    request.state.test = [x for x in range(999999)]
    #request.state.test = None
    return {"Hello": "World"}

