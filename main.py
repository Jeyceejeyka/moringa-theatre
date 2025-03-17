from database import Base, engine
from crud import get_db, add_role, add_audition, get_roles, get_auditions
from models import Role, Audition
from sqlalchemy.exc import SQLAlchemyError

def init_db():
    try:
        Base.metadata.create_all(engine)
        print("Database initialized successfully")
    except Exception as e:
        print(f"Error initializing database: {str(e)}")
        return False
    return True

def add_sample_data():
    try:
        with next(get_db()) as db:
            # Add sample role
            role = add_role(db, "Hamlet")
            print(f"Added/Retrieved role: {role.character_name}")

            # Add sample audition
            audition = add_audition(
                db=db,
                actor="John Doe",
                location="New York",
                phone=1234567890,
                role_id=role.id
            )
            print(f"Added/Retrieved audition for: {audition.actor}")

    except Exception as e:
        print(f"Error adding sample data: {str(e)}")
        return False
    return True

def main():
    if not init_db():
        return

    if not add_sample_data():
        return

    try:
        with next(get_db()) as db:
            # Display data
            roles = get_roles(db)
            auditions = get_auditions(db)
            
            print("\nCurrent Roles:")
            for role in roles:
                print(f"- {role.character_name}")
            
            print("\nCurrent Auditions:")
            for audition in auditions:
                print(f"- {audition.actor} auditioning for role_id: {audition.role_id}")
    
    except Exception as e:
        print(f"Error retrieving data: {str(e)}")

if __name__ == "__main__":
    main()
