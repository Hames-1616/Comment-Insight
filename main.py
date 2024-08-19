from fastapi import FastAPI
from gemini import getResponse
import uvicorn

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


@app.get('/evaluate')
def evaluate(comment:str):
    return {
        "Response" : getResponse(comment)
    }