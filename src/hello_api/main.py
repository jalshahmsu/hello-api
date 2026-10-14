from fastapi import FastAPI

app = FastAPI(title="hello-api")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/hello")
def hello(name: str = "World") -> dict[str, str]:
    return {"message": f"Hello, {name}!"}
