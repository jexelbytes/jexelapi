from fastapi import APIRouter, File, UploadFile
from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db
from auth.authentication import jwtBearer
from auth.db_model import User_tb
from .controllers import upload_file
from enum import Enum

router = APIRouter()

class SupportedFileTypes(str, Enum):
    images = "images"
    documents = "documents"


@router.post("/files", status_code=201)
async def post_channels_post_files(
        supported_file:SupportedFileTypes,
        comment:str = "404",
        file:UploadFile = File(...),
        db:Session = Depends(get_db),
        user:User_tb = Depends(jwtBearer(get_user=True))
    ):
    return await upload_file(
        file=file,
        comment=comment,
        user_uuid=user.uuid,
        db=db,
        supported_file=supported_file
    )