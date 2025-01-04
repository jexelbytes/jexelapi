from sqlalchemy.orm import Session
from database import Base
from datetime import datetime, date
from pydantic import BaseModel
from fastapi import HTTPException
import math


def representation_function(obj:dict, db:Session):
    return obj.__dict__

def get_generic_controller(db:Session, db_model:Base, size:int, page:int, query_params:dict = {}, order_by_created_at_desc:bool = None, representation_function:any = representation_function):
    
    query = db.query(db_model).filter(db_model.deleted_at == None)
    
    for attr, value in query_params.items():
        if type(value) == str:
            if attr in ("uuid", "id"):
                return  query.filter(getattr(db_model, attr) == value).first()
            elif ("uuid" in attr) or ("id" in attr):
                query = query.filter(getattr(db_model, attr) == value)
            else:
                query = query.filter(getattr(db_model, attr).icontains(value))
        elif type(value) in (bool, int, float, date, datetime):
            query = query.filter(getattr(db_model, attr) == value)
        elif type(value) == list:
            query = query.filter(getattr(db_model, attr).in_(value))
            print(value)
        else:
            try:
                query = query.filter(getattr(db_model, attr) == value)
            except:
                pass
    
    if order_by_created_at_desc != None:
        if order_by_created_at_desc:
            query = query.order_by(db_model.created_at.desc())
        else:
            query = query.order_by(db_model.created_at.asc())
    
    querycount = query.count()
    
    data = query.limit(size).offset(page*size).all()
    
    for item in data:
        item = representation_function(item, db)
    
    return {
        'pages':    math.ceil(querycount/size),
        'items':    querycount,
        'data':     data
    }

def post_generic_controller(db:Session, db_model:Base, create_schema:BaseModel, created_by:str = None):
    new_row = db_model(**create_schema.model_dump())
    if created_by:
        new_row.created_by = created_by
    
    db.add(new_row)
    db.commit()
    db.refresh(new_row)
    return new_row

def put_generic_controller(db:Session, db_model:Base, uuid:str, update_schema:BaseModel):
    query = db.query(db_model).filter(db_model.deleted_at == None).filter(db_model.uuid == uuid).first()
    
    if not query:
        raise RowNotFoundException(tablename=db_model.__tablename__)
    
    data = update_schema.model_dump(exclude_none=True)
    
    if data.items().__len__() < 1:
        raise EmptyUpdateQueryException()
    
    for key, value in data.items():
        setattr(query, key, value)
    
    db.add(query)
    db.commit()
    db.refresh(query)
    
    return query

def delete_generic_controller(db:Session, db_model:Base, uuid:str):
    query = db.query(db_model).filter(db_model.deleted_at == None).filter(db_model.uuid == uuid).first()
    
    if query:
        query.deleted_at = datetime.now()
        db.add(query)
        db.commit()
        db.refresh(query)
    else:
        raise RowNotFoundException(tablename=db_model.__tablename__)
    
    return query

class RowNotFoundException(Exception):
    def __init__(self, tablename:str):
        raise HTTPException(status_code=404, detail=f"{tablename} not found.")
    
class EmptyUpdateQueryException(Exception):
    def __init__(self):
        raise HTTPException(status_code=400, detail=f"Update query is empty.")
    
class NoChurchLogedException(Exception):
    def __init__(self):
        raise HTTPException(status_code=400, detail=f"You need to be logged into a church.")