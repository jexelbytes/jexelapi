from auto_alembic import Automatic_Alembic
from config import host, port, is_develop

if __name__ == '__main__':
    import uvicorn
    
    alembic = Automatic_Alembic()
    print(alembic.automatic_migrate())
    
    if is_develop:
        uvicorn.run("app:app", host=host, port=port, reload=True)
    else:
        uvicorn.run("app:app", host=host, port=port)