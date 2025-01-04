from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db
from auth.authentication import jwtBearer
from basic_controller import get_generic_controller, post_generic_controller, put_generic_controller, delete_generic_controller
from .schema import Create{{ class_name }}_sch, Update{{ class_name }}_sch
from .db_model import {{ class_name }}_tbl
from auth.db_model import ActiveSession_tb
from .controller import {{ table_name }}_representation

router = APIRouter()

@router.get("/{{ table_name }}", dependencies=[Depends(jwtBearer())])
def get_event(
    size:int = 10,
    page:int = 0,
    db:Session = Depends(get_db),
):
    query_params = {
    }
    response = get_generic_controller(
        db_model={{ class_name }}_tbl,
        db=db,
        query_params=query_params,
        size=size,
        page=page
    )
    
    for item in response['data']:
        item = {{ table_name }}_representation(item=item)
        
    return response

@router.post("/{{ module_name }}", status_code=201)
def post_{{ table_name }}(data:Create{{ class_name }}_sch, db:Session = Depends(get_db), session:ActiveSession_tb = Depends(jwtBearer(get_session=True))):
    return post_generic_controller(db_model={{ class_name }}_tbl, create_schema=data, db=db, created_by=session.user_uuid)

@router.put("/{{ module_name }}", dependencies=[Depends(jwtBearer())])
def put_{{ table_name }}(uuid:str, data:Update{{ class_name }}_sch, db:Session = Depends(get_db)):
    return put_generic_controller(db_model={{ class_name }}_tbl, uuid=uuid, update_schema=data, db=db)

@router.delete("/{{ module_name }}", dependencies=[Depends(jwtBearer())])
def delete_{{ table_name }}(uuid:str, db:Session = Depends(get_db)): return delete_generic_controller(db_model={{ class_name }}_tbl, uuid=uuid, db=db)