from fastapi import FastAPI, Form

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "FastAPI is running!"}

@app.post("/submit")
async def receive_from_roblox(value: str = Form(...)):
    print(f"Received value from Roblox: {value}")
    return {"received": value}
