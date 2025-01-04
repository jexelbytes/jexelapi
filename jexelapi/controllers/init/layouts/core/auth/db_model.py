from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql.sqltypes import *
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.sql import func
from uuid import uuid4
from database import Base
from files.db_model import Files_db

class User_tb(Base):
    __tablename__ = "users"

    uuid = Column(UUID(as_uuid=True), primary_key=True, nullable=False, unique=True, index=True, default=uuid4)
    
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    
    is_superuser = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, nullable=False, default=func.now())
    deleted_at = Column(DateTime, nullable=True)
    
    avatar_ref: Mapped['Files_db'] = relationship(Files_db)

class ActiveSession_tb(Base):
    __tablename__ = "active_session"
        
    token = Column(String, primary_key=True, nullable=False, unique=True, index=True)
    firebase_token = Column(String, nullable=True)
    user_uuid = Column(UUID(as_uuid=True), ForeignKey('users.uuid'), nullable=True, index=True)
    
    expire_at = Column(DateTime, nullable=False)
    logout_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=False, default=func.now())
    
    user_ref: Mapped['User_tb'] = relationship(User_tb)
    
    def representation(self):
        data = self.__dict__
        try:
            data.pop('firebase_token')
        except:
            pass
        
        try:
            data.pop('token')
        except:
            pass
        
        return data