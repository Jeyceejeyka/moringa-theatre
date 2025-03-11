from database import Base, engine
from crud import get_db  # Import get_db function
from models import Role, Audition
from crud import add_role, add_audition, get_roles, get_auditions

# Create tables
Base.metadata.create_all(engine)

# Add sample data
with next(get_db()) as db:  # Use the database session
    # Check if the role already exists
    existing_role = db.query(Role).filter_by(character_name="Hamlet").first()
    print("Existing Role:", existing_role)  # Debug statement to check existing role
    if not existing_role:
        role = add_role(db, "Hamlet")
    else:
        role = existing_role

    # Check if the audition already exists for the role
    existing_audition = db.query(Audition).filter_by(actor="John Doe", role_id=role.id).first()
    print("Existing Audition:", existing_audition)  # Debug statement to check existing audition
    if not existing_audition:
        audition = add_audition(db, "John Doe", "New York", 1234567890, role.id)

# Fetch and display data
with next(get_db()) as db:  # Use the database session
    roles = get_roles(db)
    auditions = get_auditions(db)
    print("Roles:", [role.character_name for role in roles])
    print("Auditions:", [(audition.actor, audition.location, audition.phone) for audition in auditions])
