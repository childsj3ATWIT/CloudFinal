import flask
from fastapi import FastAPI, Cookie, Request
from pydantic import BaseModel
from fastapi.responses import Response

from CloudProject.bff.main import app


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
async def login(response: Response):
    response.set_cookie(key="username", value="flask", secure=True, httponly=True)#, samesite="Lax")
    return {"message": "Cookie set"}

#need to add a user database, can be done later.
#can maybe add a session token later, or password authentication.