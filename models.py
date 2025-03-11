from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from database import Base

class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    character_name = Column(String, nullable=False, unique=True)  # Enforce uniqueness
    auditions = relationship("Audition", back_populates="role", cascade="all, delete-orphan")
    
    def actors(self):
        return [audition.actor for audition in self.auditions]
    
    def locations(self):
        return [audition.location for audition in self.auditions]
    
    def lead(self):
        hired_auditions = [audition for audition in self.auditions if audition.hired]
        return hired_auditions[0] if hired_auditions else "No actor has been hired for this role."
    
    def understudy(self):
        hired_auditions = [audition for audition in self.auditions if audition.hired]
        return hired_auditions[1] if len(hired_auditions) > 1 else "No actor has been hired for understudy for this role."

class Audition(Base):
    __tablename__ = 'auditions'
    id = Column(Integer, primary_key=True)
    actor = Column(String, nullable=False)
    __table_args__ = (UniqueConstraint('actor', 'role_id', name='uq_actor_role'),)  # Enforce uniqueness
    location = Column(String, nullable=False)
    phone = Column(Integer, nullable=False)
    hired = Column(Boolean, default=False)
    role_id = Column(Integer, ForeignKey('roles.id'))
    role = relationship("Role", back_populates="auditions")
    
    def call_back(self):
        self.hired = True
