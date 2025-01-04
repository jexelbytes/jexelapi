from fastapi import File, UploadFile, HTTPException
from sqlalchemy.orm import Session
from .db_model import Files_db
from auth.db_model import User_tb
from .exceptions import  UnsuportedFileTypeException
from uuid import uuid4
from services.s3_service import s3_upload
from config import AWS_S3_BUCKET, AWS_S3_ZONE

async def get_files_controller(id:str, db:Session):
    search = db.query(Files_db)
    
    if id:
        search = search.filter(Files_db.id == id)
    
    return search.all()

async def create_avatar_controller(file:UploadFile, db:Session, user:User_tb):
    
    file = await upload_file(file=file, comment=None, user_uuid=user.uuid, db=db, supported_file='images')
    file_id = file.id
    db.refresh(user)
    user.avatar = file_id
    db.add(user)
    db.commit()
    db.refresh(file)
    
    return file

async def upload_file(file: File, comment:str, user_uuid:str, db:Session, supported_file:str = None) -> Files_db | str:
    """supported_file_type accepts 'images' and 'documents'"""
    
    content = await file.read()
    folder = suported_file_type(file.filename)
    
    if (supported_file != None) and (folder != supported_file):
        raise HTTPException(status_code=400, detail=f"Unsuported file type, expected a {supported_file.replace('s','')}.")

    query = Files_db()
    query.comment = comment
    query.ext = file.filename.split('.')[-1].lower()
    query.name = f'{uuid4()}.{query.ext}'
    query.folder = folder
    query.path = f'https://s3.{AWS_S3_ZONE}.amazonaws.com/{AWS_S3_BUCKET}/{folder}/{query.name}'
    query.size = file.size
    query.created_by = user_uuid
    
    await s3_upload(contents = content, key = f"{folder}/{query.name}", Content_Type=file.content_type)
    
    db.add(query)
    db.commit()
    db.refresh(query)

    return query

supported_img_filetypes = ['img', 'jpeg', 'jpg', 'png', 'bmp']
supported_document_filetypes = ['doc', 'docx', 'pdf', 'xlsx', 'pptx']

def suported_file_type(filename:str):

    type = filename.split(".")[-1]

    if type.lower() in supported_img_filetypes:
        return 'images'
    elif type.lower() in supported_document_filetypes:
        return 'documents'
    else:
        raise UnsuportedFileTypeException()