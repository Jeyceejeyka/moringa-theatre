import pytest
from models import Role, Audition
from database import Base, engine, SessionLocal

@pytest.fixture
def session():
    Base.metadata.create_all(engine)
    session = SessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(engine)

def test_role_creation(session):
    role = Role(character_name="Hamlet")
    session.add(role)
    session.commit()
    assert role.id is not None
    assert role.character_name == "Hamlet"
    assert role.auditions == []

def test_audition_creation(session):
    role = Role(character_name="Hamlet")
    session.add(role)
    session.commit()
    
    audition = Audition(
        actor="John Doe",
        location="New York",
        phone="1234567890",
        role=role
    )
    session.add(audition)
    session.commit()
    
    assert audition.actor == "John Doe"
    assert audition.role.character_name == "Hamlet"
    assert not audition.hired

def test_role_relationships(session):
    role = Role(character_name="Hamlet")
    session.add(role)
    
    audition1 = Audition(actor="John", location="NY", phone="123", role=role)
    audition2 = Audition(actor="Jane", location="LA", phone="456", role=role)
    session.add_all([audition1, audition2])
    session.commit()
    
    assert len(role.auditions) == 2
    assert "John" in role.actors()
    assert "NY" in role.locations()

def test_lead_and_understudy(session):
    role = Role(character_name="Hamlet")
    session.add(role)
    
    audition1 = Audition(actor="John", location="NY", phone="123", role=role)
    audition2 = Audition(actor="Jane", location="LA", phone="456", role=role)
    session.add_all([audition1, audition2])
    session.commit()
    
    assert isinstance(role.lead(), str)  # No hired actors yet
    
    audition1.call_back()  # Hire first actor
    assert role.lead() == audition1
    assert isinstance(role.understudy(), str)
    
    audition2.call_back()  # Hire second actor
    assert role.understudy() == audition2