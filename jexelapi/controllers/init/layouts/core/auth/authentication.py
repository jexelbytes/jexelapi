from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from config import JWT_SECRET, JWT_ALGORITHM
from fastapi import Depends, Request
from .exceptions import InvalidOrExpiredToken, ExpiredRefreshException, UserNotFoundException
from datetime import datetime, timedelta
import jwt
from .db_model import User_tb, ActiveSession_tb
from sqlalchemy.orm import Session
from database import get_db
from config import JWT_SECRET, JWT_EXPIRE_TIME, JWT_REFRESH_EXPIRE_TIME
import hashlib
from files.db_model import Files_db

def search_user_controller(uuid:str, db:Session):
  user = db.query(User_tb).filter(User_tb.uuid == uuid).first()
  if not user:
    raise UserNotFoundException()
  else:
    return user_representation(user=user, db=db, strict=True)

def user_representation(user: User_tb, db:Session = None, strict:bool = False):
    if user:
      user = user.__dict__
      
      if db:
          try:
              user['avatar'] = db.query(Files_db).filter(Files_db.id == user.get('avatar')).first().path
          except:
              pass
          try:
              user['background'] = db.query(Files_db).filter(Files_db.id == user.get('background')).first().path
          except:
              pass
            
      user.pop('hashed_password')
      
      if strict:
          user.pop('created_at')
      
      return user
    else: return None

def login(db:Session, user:User_tb = None, firebase_token:str = None):
    
  expire_time = datetime.now() + timedelta(hours=JWT_EXPIRE_TIME)
  expire_refresh = datetime.now() + timedelta(hours=JWT_REFRESH_EXPIRE_TIME)
  
  payload = {
    "expiry": expire_time.strftime('%y-%m-%d %H:%M:%S')
  }
  
  if user:
    payload['user_uuid'] = str(user.uuid)
  
  token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
  
  payload['expiry'] = expire_refresh.strftime('%y-%m-%d %H:%M:%S')
  
  refresh = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
  
  session = ActiveSession_tb()
  if user:
    session.user_uuid = user.uuid
  session.token = str(token)
  session.expire_at = expire_time
  session.firebase_token = firebase_token
  
  db.add(session)
  db.commit()
  
  if user:
    db.refresh(user)
    
  response = { 'access_token': token, 'refresh': refresh , 'user_data':user_representation(user=user, db=db) }
  
  return response

def refresh(refresh:str, db:Session = Depends(get_db)):
  payload = decodeJWT(token=refresh)
  
  if payload == None:
    raise InvalidOrExpiredToken()
  
  if datetime.strptime(payload['expiry'], '%y-%m-%d %H:%M:%S') > datetime.now():
    
    user = db.query(User_tb).filter(User_tb.uuid == payload['userUUID']).first()
    
    return login(user=user, db=db)
  else:
    raise ExpiredRefreshException()

def decodeJWT(token: str):
  try:
    decode_token = jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHM)
    return decode_token
  except:
    return None
  
def hash_password(password: str):
    result = hashlib.md5(password.encode())
    return str(result.hexdigest())

class jwtBearer(HTTPBearer):

  get_user:bool = False
  get_session:bool = False
  get_token:bool = False

  need_superuser:bool = False

  def __init__(self, auto_Error : bool = True, get_user:bool = False, get_session:bool = False, get_token:bool = False, need_superuser:bool = False):
    super(jwtBearer, self).__init__(auto_error=auto_Error)
    self.get_user = get_user
    self.get_session = get_session
    self.get_token = get_token
    self.need_superuser = need_superuser
    
  async def __call__(self, request : Request, db:Session = Depends(get_db)):
    credentials: HTTPAuthorizationCredentials = await super(jwtBearer, self).__call__(request)
    
    session = self.verify_jwt(credentials.credentials, db=db)
    
    if not session:
      raise InvalidOrExpiredToken()

    if self.need_superuser:
      if not session.user_ref.is_superuser:
        raise InvalidOrExpiredToken()

    if self.get_user:
      active_session = db.query(ActiveSession_tb).filter(ActiveSession_tb.token == credentials.credentials).first()
      return active_session.user_ref

    if self.get_session:
      return session
    
    if self.get_token:
      return credentials.credentials
      
  def verify_jwt(self, jwtoken:str, db:Session) -> ActiveSession_tb:
    token = decodeJWT(token=jwtoken)

    if not token:
        return False

    if datetime.strptime(token['expiry'], '%y-%m-%d %H:%M:%S') < datetime.now():
        return False
      
    session = db.query(ActiveSession_tb).filter(ActiveSession_tb.token == jwtoken).first()
    if not session:
        return False

    return session