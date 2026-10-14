from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI(title="hello-api")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/hello")
def hello(
    name: Annotated[str, Query(max_length=50)] = "World",
) -> dict[str, str]:
    return {"message": f"Hello, {name}!"}
