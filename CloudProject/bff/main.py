from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
import mysql.connector

app = FastAPI()

def get_db():
    return mysql.connector.connect(
        host="db",
        user="mgs_user",
        password="pa55word",
        database="my_guitar_shop"
    )

@app.get("/", response_class=HTMLResponse)
def home():
    return "<h1>Welcome to the Guitar Shop</h1>"

@app.get("/products")
def products(db=Depends(get_db)):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products")
    return cursor.fetchall()
