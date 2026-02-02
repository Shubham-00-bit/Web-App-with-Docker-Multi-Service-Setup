from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "Backend is healthy 🚀"}

@app.get("/db")
def db_check():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )
    cur = conn.cursor()
    cur.execute("SELECT 1;")
    return {"db": "connected"}
