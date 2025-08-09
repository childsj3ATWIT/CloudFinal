from fastapi import FastAPI, Depends, UploadFile, File, Form, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import mysql.connector
import redis
import smtplib
from email.mime.text import MIMEText
import boto3
from botocore.client import Config
import os

app = FastAPI()

# CORS configuration
# Allow requests from the frontend running on localhost:8080
origins = ["*"],

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MySQL connection
def get_db():
    return mysql.connector.connect(
        host="db",
        user="mgs_user",
        password="pa55word",
        database="my_guitar_shop"
    )

# Redis client
redis_client = redis.Redis(host="redis", port=6379)

# MinIO (S3-compatible)
minio_client = boto3.client(
    "s3",
    endpoint_url="http://minio:9000",
    aws_access_key_id=os.getenv("MINIO_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("MINIO_SECRET_KEY"),
    config=Config(signature_version='s3v4'),
    region_name='us-east-1'
)

# Email via Postfix
def send_email(to_address: str, subject: str, content: str):
    msg = MIMEText(content)
    msg["Subject"] = subject
    msg["From"] = "noreply@guitarshop.local"
    msg["To"] = to_address
    with smtplib.SMTP("email", 25) as server:
        server.send_message(msg)

@app.get("/")
def root():
    return {"message": "Guitar Shop BFF API"}

@app.get("/products")
def get_products(db=Depends(get_db)):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products")
    return cursor.fetchall()

@app.post("/login")
def login(email: str = Form(...), password: str = Form(...)):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM customers WHERE email_address = %s AND password = %s", (email, password))
    user = cursor.fetchone()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    session_token = f"session_{user['customer_id']}"
    redis_client.set(session_token, user['email_address'], ex=3600)
    return {"cookie": session_token}

@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    bucket = "guitarshop"
    try:
        minio_client.create_bucket(Bucket=bucket)
    except:
        pass
    minio_client.upload_fileobj(file.file, bucket, file.filename)
    return {"message": f"Uploaded {file.filename}"}

@app.post("/notify")
def notify(email: str = Form(...)):
    send_email(email, "Guitar Shop Notification", "Thanks for visiting the Guitar Shop!")
    return {"message": "Email sent"}
