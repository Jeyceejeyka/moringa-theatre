from models import Role, Audition
from database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

session = next(get_db())

def add_role(db, character_name):
    existing_role = db.query(Role).filter_by(character_name=character_name).first()
    print("Debug: Existing Role Check:", existing_role)  # Debug statement
    if not existing_role:
        role = Role(character_name=character_name)
        db.add(role)
        db.commit()
        return role
    return existing_role


def add_audition(db, actor, location, phone, role_id):
    existing_audition = db.query(Audition).filter_by(actor=actor, role_id=role_id).first()
    print("Debug: Existing Audition Check:", existing_audition)  # Debug statement
    if not existing_audition:
        audition = Audition(actor=actor, location=location, phone=phone, role_id=role_id)
        db.add(audition)
        db.commit()
        return audition
    return existing_audition

def get_roles(db):
    return db.query(Role).all()

def get_auditions(db):
    return db.query(Audition).all()
