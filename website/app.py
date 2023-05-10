"""run with
uvicorn website.app:app --reload
"""

import AQAInterpreter  # type: ignore
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()


class Code(BaseModel):
    code: str
    transpile: bool = False


@app.post("/api/run")
def main(code: Code):
    "Takes in AQA pseudo-code and returns the output."
    return AQAInterpreter.run(code.code, transpile=code.transpile)


app.mount("/", StaticFiles(directory="website/static", html=True), name="static")
