from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship
from src.database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
    
class Cv(Base):
    __tablename__ = "cv"
    id = Column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4(), index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'))
    telephone = Column(Integer, index=True)
    role = Column(String, index=True)
    summary= Column(Text, unique=True, index=True)
    
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)
    
    user = relationship("User", back_populates="cv")
    experences = relationship("Experence", back_populates="cv", cascade="all, delete-orphan")  
    skills = relationship("Skill", back_populates="cv", cascade="all, delete-orphan")
    soft_skills = relationship("Soft_Skill", back_populates="cv", cascade="all, delete-orphan")
    certifications = relationship("Certifications", back_populates="cv", cascade="all, delete-orphan")
    academics = relationship("Academic", back_populates="cv", cascade="all, delete-orphan")
    profiles = relationship("Profile", back_populates="cv", cascade="all, delete-orphan")
    languages = relationship("Language", back_populates="cv", cascade="all, delete-orphan")
    
    
class Experence(Base):
    __tablename__ = "experence"
    id = Column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4(), index=True)
    cv_id = Column(UUID(as_uuid=True), ForeignKey('cv.id', ondelete='CASCADE'))

    role = Column(String, index=True)
    company = Column(Text, index=True)
    description = Column(Text, index=True)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)
    
    cv = relationship("Cv", back_populates="experence")
    
class Skill(Base):
    __tablename__ = "skill" 
    id = Column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4(), index=True)
    cv_id = Column(UUID(as_uuid=True), ForeignKey('cv.id', ondelete='CASCADE'))
    
    title = Column(String, index=True)
    level = Column(String, index=True)
    
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)
    
    cv = relationship("Cv", back_populates="skill")
    
class Soft_Skill(Base):
    __tablename__ = "soft_skill"
    id = Column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4(), index=True)
    cv_id = Column(UUID(as_uuid=True), ForeignKey('cv.id', ondelete='CASCADE'))
    
    title = Column(String, index=True)
    
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)
    
    cv = relationship("Cv", back_populates="soft_skill")
    
class Certifications(Base):
    __tablename__ = "certifications"
    id = Column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4(), index=True)
    cv_id = Column(UUID(as_uuid=True), ForeignKey('cv.id', ondelete='CASCADE'))
    
    name = Column(String, index=True)
    institution = Column(String, index=True)
    description = Column(Text, index=True)
    date = Column(DateTime)
    
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)
    
    cv = relationship("Cv", back_populates="certifications")
    
class Academic(Base):
    __tablename__ = "academic"
    id = Column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4(), index=True)
    cv_id = Column(UUID(as_uuid=True), ForeignKey('cv.id', ondelete='CASCADE'))
    
    title = Column(String, index=True)
    institution = Column(String, index=True)
    description = Column(Text, index=True)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)
    
    cv = relationship("Cv", back_populates="academic")

class Profile(Base):
    __tablename__ = "profile"
    id = Column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4(), index=True)
    cv_id = Column(UUID(as_uuid=True), ForeignKey('cv.id', ondelete='CASCADE'))
    
    name = Column(String, index=True)
    url = Column(String, index=True)
    
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)
    
    cv = relationship("Cv", back_populates="profile")
    
class Language(Base):
    __tablename__ = "language"
    id = Column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4(), index=True)
    cv_id = Column(UUID(as_uuid=True), ForeignKey('cv.id', ondelete='CASCADE'))
    
    speech = Column(String, index=True)
    level = Column(String, index=True)
    
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)
    
    cv = relationship("Cv", back_populates="language")