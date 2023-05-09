from fastapi import FastAPI
import uvicorn
from model import get_db, session_scope, Film
from faker import Faker
import time

Faker.seed(time.time())
fake = Faker()

app = FastAPI()


@app.get("/no_scope")
async def no_scope():
    for i in range(1, 100):
        db = get_db()
        films = db.query(Film).limit(10).all()

    return {"message": "OK"}

@app.get("/scope")
async def scope():
    for i in range(1, 100):
        with session_scope() as db:
            films = db.query(Film).limit(10).all()

    return {"message": "OK"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8888)
