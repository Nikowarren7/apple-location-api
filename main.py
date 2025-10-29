from fastapi import FastAPI, Request
from datetime import datetime

app = FastAPI()

# In-memory log store
logs = []

@app.get("/")
def home():
    return {"status": "Apple location API online"}

@app.post("/location")
async def receive_location(request: Request):
    """Receives location data from Apple Shortcut and stores it in memory."""
    data = await request.json()
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "data": data
    }
    logs.append(entry)
    return {"status": "received", "timestamp": entry["timestamp"], "data": data}

@app.get("/logs")
def get_logs():
    """Return the 10 most recent location entries."""
    return {"count": len(logs), "data": logs[-10:]}

@app.get("/latest")
def get_latest():
    """Return only the most recent location entry."""
    if not logs:
        return {"status": "no data yet"}
    return logs[-1]
