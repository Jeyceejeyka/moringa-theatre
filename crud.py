from models import Role, Audition
from database import SessionLocal
from sqlalchemy.exc import SQLAlchemyError

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def add_role(db, character_name: str):
    try:
        existing_role = db.query(Role).filter_by(character_name=character_name).first()
        if not existing_role:
            role = Role(character_name=character_name)
            db.add(role)
            db.commit()
            db.refresh(role)
            return role
        return existing_role
    except SQLAlchemyError as e:
        db.rollback()
        raise Exception(f"Error adding role: {str(e)}")

def add_audition(db, actor: str, location: str, phone: int, role_id: int):
    try:
        existing_audition = db.query(Audition).filter_by(actor=actor, role_id=role_id).first()
        if not existing_audition:
            audition = Audition(
                actor=actor,
                location=location,
                phone=phone,
                role_id=role_id
            )
            db.add(audition)
            db.commit()
            db.refresh(audition)
            return audition
        return existing_audition
    except SQLAlchemyError as e:
        db.rollback()
        raise Exception(f"Error adding audition: {str(e)}")

def get_roles(db):
    return db.query(Role).all()

def get_auditions(db):
    return db.query(Audition).all()
