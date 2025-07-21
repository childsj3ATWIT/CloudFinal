from fastapi import FastAPI, Request, HTTPException

app = FastAPI()

@app.get("/verify")
def verify(cookie: str):
    if cookie == "valid_session_token":
        return {"user": "verified"}
    raise HTTPException(status_code=403, detail="Invalid session")
