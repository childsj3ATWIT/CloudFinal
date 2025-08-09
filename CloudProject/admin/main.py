from fastapi import FastAPI, HTTPException, Form
import mysql.connector

app = FastAPI()

def get_db():
    return mysql.connector.connect(
        host="db",
        user="mgs_user",
        password="pa55word",
        database="my_guitar_shop"
    )

@app.get("/admin")
def read_root():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SHOW DATABASES")
    databases = cursor.fetchall()


@app.get("/admin/products")
def all_products():
    db = get_db()
    cur = db.cursor(dictionary=True)
    cur.execute("SELECT * FROM products")
    return cur.fetchall()

@app.post("/admin/add")
def add_product(name: str = Form(...), price: float = Form(...), code: str = Form(...)):
    db = get_db()
    cur = db.cursor()
    cur.execute(
        "INSERT INTO products (category_id, product_code, product_name, description, list_price, discount_percent) VALUES (1, %s, %s, 'N/A', %s, 0)",
        (code, name, price)
    )
    db.commit()
    return {"message": "Product added"}
