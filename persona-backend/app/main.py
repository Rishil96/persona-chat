from fastapi import FastAPI


app = FastAPI(title="Persona")


@app.get("/health")
def health():
    return {"status": "ok"}
