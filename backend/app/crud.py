from sqlalchemy.orm import Session
from app import models, schemas

def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, username: str):
    user = models.User(username=username)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def create_session(db: Session, user_id: int):
    session = models.Session(user_id=user_id)
    db.add(session)
    db.commit()
    db.refresh(session)
    return session

def add_message(db: Session, session_id: int, role: str, content: str):
    msg = models.Message(session_id=session_id, role=role, content=content)
    db.add(msg)
    db.commit()
    db.refresh(msg)
    return msg
