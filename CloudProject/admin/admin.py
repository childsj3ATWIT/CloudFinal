from fastapi import FastAPI
app = FastAPI()

@app.get("/admin")
def panel():
    return {"message": "Admin panel loaded"}
