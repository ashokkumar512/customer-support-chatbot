from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.User)
def create_user(username: str, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, username)
    if db_user:
        return db_user
    return crud.create_user(db, username)

@app.post("/users/{user_id}/sessions/", response_model=schemas.Session)
def create_session(user_id: int, db: Session = Depends(get_db)):
    return crud.create_session(db, user_id)

@app.post("/sessions/{session_id}/messages/")
def add_message(session_id: int, message: schemas.MessageCreate, db: Session = Depends(get_db)):
    return crud.add_message(db, session_id, message.role, message.content)
