from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "AnalitycsP2P backend funcionando correctamente"}
    uvicorn backend.main:app --host 0.0.0.0 --port 8000
