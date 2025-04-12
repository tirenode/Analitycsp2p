
# Main entry point
from backend.main import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
uvicorn backend.main:app --host 0.0.0.0 --port 8000
