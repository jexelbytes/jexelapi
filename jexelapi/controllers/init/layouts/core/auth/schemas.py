from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class auth_sch(BaseModel):
    email: EmailStr | None = None
    password: str | None = None
    firebase_token: str | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "email": "person@email.com",
                    "password": "12345678",
                    "firebase_token": "firebase_token"
                }
            ]
        }
    }
    
  
class CreateUser(BaseModel):
    first_name: Optional[str] = Field(min_length=1, max_length=128, default=None)
    last_name: Optional[str] = Field(min_length=1, max_length=128, default=None)
    phone:str | None = None
    email: EmailStr
    hashed_password: str = Field(min_length=8, max_length=128, default=None)
    
  
class UpdateUser(BaseModel):
    first_name: Optional[str] = Field(min_length=1, max_length=128, default=None)
    last_name: Optional[str] = Field(min_length=1, max_length=128, default=None)
    phone:str | None = None
    email: EmailStr | None = None
    

class CreateUserAdmin(BaseModel):
    first_name: Optional[str] = Field(min_length=1, max_length=128, default=None)
    last_name: Optional[str] = Field(min_length=1, max_length=128, default=None)
    phone:str | None = None
    email: EmailStr
    hashed_password: str = Field(min_length=8, max_length=128, default=None)
    avatar:int | None = None

class UpdateUserAdmin(BaseModel):
    first_name: Optional[str] = Field(min_length=1, max_length=128, default=None)
    last_name: Optional[str] = Field(min_length=1, max_length=128, default=None)
    phone:str | None = None
    email: EmailStr | None = None
    avatar:int | None = None

class UpdateUserPassword(BaseModel):
  new_password: str = Field(min_length=8, max_length=128, default=None)
  old_password: str = Field(min_length=8, max_length=128, default=None)

class refresh_sch(BaseModel):
  token: str
  
class FirebaseToken(BaseModel):
  firebase_token: str
