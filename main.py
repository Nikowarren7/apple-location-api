from fastapi import FastAPI, Request
from datetime import datetime

app = FastAPI()

# just a test
@app.get("/")
def root():
    return {"status": "ok", "message": "API is live!"}

# new endpoint to receive location
@app.post("/location")
async def receive_location(request: Request):
    data = await request.json()
    print("📍 Location update:", data)  # shows up in Render logs
    return {
        "status": "received",
        "timestamp": datetime.utcnow().isoformat(),
        "data": data
    }
