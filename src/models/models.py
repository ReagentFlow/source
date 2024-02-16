from sqlalchemy import Integer, String, TIMESTAMP, ForeignKey, Column, JSON, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class reagent(Base):
    __tablename__ = 'reagent'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    cas_number = Column(String, nullable=False)
    mass = Column(Integer, nullable=False)


class contaner(Base):
    __tablename__ = 'contaner'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    cas_number = Column(String, nullable=False)
    mass = Column(Integer, nullable=False)
    mass_contaner = Column(Integer, nullable=False)

class role(Base):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    permissions = Column(JSON)


class user(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    role_id = Column(Integer, ForeignKey("role.id"))
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(
        Boolean, default=False, nullable=False
    )
    is_verified = Column(
        Boolean, default=False, nullable=False
    )