from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql.sqltypes import *
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.sql import func
from uuid import uuid4
from database import Base
from auth.db_model import User_tb

class {{ class_name }}_tbl(Base):
    __tablename__ = "{{ table_name }}"
    uuid = Column(UUID(as_uuid=True), primary_key=True, nullable=False, unique=True, index=True, default=uuid4)
    
    created_by =        Column(UUID(as_uuid=True), ForeignKey("users.uuid"))
    created_at =        Column(DateTime, default=func.now())
    deleted_at =        Column(DateTime, nullable=True, default=None)
    
    user_ref: Mapped['User_tb'] = relationship(User_tb)