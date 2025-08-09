import flask
from MySQLdb.constants.ER import USERNAME
from fastapi import FastAPI, Cookie, Request, Form, HTTPException, status
from pydantic import BaseModel
from fastapi.responses import Response
app = FastAPI()
#from CloudProject.bff.main import app

USERS = {
    "admin": "adminpass",
    "user1": "user1pass"
}

@app.get("/read_cookie")
async def read_cookie(username: str = Cookie(None)):
    return {"username": username}

@app.get("/headers/")
async def get_headers(request: Request):
    user_agent = request.headers.get("user-agent")
    user_email = request.headers.get("user_email")

    return {
        "User-Agent": user_agent,
        "user_email": user_email
    }

@app.post("/login")
async def login(response: Response, username: str = Form(...), password: str = Form(...)):
    if USERS.get(username) == password:
        response.set_cookie(key="username", value=username, httponly=True, secure=True)
        return {"message": f"Logged in as {username}"}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

#@app.post("/login")
#async def login(response: Response, username: str = Form(...), password: str = Form(...)):
#    if USERS.get(username) == password:
#        response.set_cookie(key="username", value=username, httponly=True)
#        return {"message": f"Logged in as {username}"}
#    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

@app.post("/logout")
async def logout(response: Response):
    response.delete_cookie(key="username")
    return {"message": "Logged out"}




#need to add a user database, can be done later.
#can maybe add a session token later, or password authentication.