from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from database import Base
from typing import List, Optional, Union

class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    character_name = Column(String, nullable=False, unique=True)
    auditions = relationship("Audition", back_populates="role", cascade="all, delete-orphan")
    
    def actors(self) -> List[str]:
        """Returns list of actor names for this role"""
        return [audition.actor for audition in self.auditions]
    
    def locations(self) -> List[str]:
        """Returns list of audition locations for this role"""
        return [audition.location for audition in self.auditions]
    
    def lead(self) -> Union[str, 'Audition']:
        """Returns first hired audition or message if none found"""
        hired_auditions = [a for a in self.auditions if a.hired]
        if not hired_auditions:
            return 'no actor has been hired for this role'
        return hired_auditions[0]
    
    def understudy(self) -> Union[str, 'Audition']:
        """Returns second hired audition or message if none found"""
        hired_auditions = [a for a in self.auditions if a.hired]
        if len(hired_auditions) < 2:
            return 'no actor has been hired for understudy for this role'
        return hired_auditions[1]

    def __repr__(self) -> str:
        return f"<Role(character_name='{self.character_name}')>"

class Audition(Base):
    __tablename__ = 'auditions'
    id = Column(Integer, primary_key=True)
    actor = Column(String(100), nullable=False)
    location = Column(String(100), nullable=False)
    phone = Column(String(15), nullable=False)
    hired = Column(Boolean, default=False)
    role_id = Column(Integer, ForeignKey('roles.id', ondelete='CASCADE'))
    role = relationship("Role", back_populates="auditions")
    
    __table_args__ = (
        UniqueConstraint('actor', 'role_id', name='uq_actor_role'),
    )
    
    def call_back(self) -> None:
        """Changes hired status to True"""
        self.hired = True
    
    def __repr__(self) -> str:
        return f"<Audition(actor='{self.actor}', role_id={self.role_id})>"
