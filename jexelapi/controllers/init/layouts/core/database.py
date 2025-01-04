from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import db_type, db_user, db_pass, db_host, db_port, db_name
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

# Conexion a base de datos
sqlalchemy_url = f"{db_type}://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"

engine = create_engine(sqlalchemy_url, connect_args={"options": f"-c timezone=America/Santiago"}, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()