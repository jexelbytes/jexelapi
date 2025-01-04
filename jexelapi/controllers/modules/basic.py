from controllers.utilities import render_file, appendtextfile
import shutil
import os

def create_basic_module(name:str):
    dir = f"./src/{name}"
    layouts_path = "./controllers/modules/layout/basic"
    
    os.mkdir(dir)
    
    shutil.copy(f"{layouts_path}/db_model.py", f"{dir}/db_model.py")
    shutil.copy(f"{layouts_path}/router.py", f"{dir}/router.py")
    shutil.copy(f"{layouts_path}/schema.py", f"{dir}/schema.py")
    shutil.copy(f"{layouts_path}/controller.py", f"{dir}/controller.py")

    ctx = {
        "class_name": create_class_name(name=name),
        "table_name": name.lower()
    }
    
    render_file(path=f"{dir}/db_model.py", ctx=ctx)
    render_file(path=f"{dir}/router.py", ctx=ctx)
    render_file(path=f"{dir}/schema.py", ctx=ctx)
    render_file(path=f"{dir}/controller.py", ctx=ctx)
    
    import_string_app = f'\nfrom {name}.router import router as {name}_router\napp.include_router({name}_router, tags=["{create_tag_name(name=name)}"], prefix="/api")\n'
    import_string_models = f'\nfrom {name}.db_model import *\n'
    
    appendtextfile(path="./src/app.py", text=import_string_app)
    appendtextfile(path="./src/models.py", text=import_string_models)
    
    print("Done!")
    
def create_class_name(name:str):
    splited = name.split("_")
    list_words = []
    for item in splited:
        list_words.append(item.capitalize())
        
    name ="".join(list_words)
    
    return name

def create_tag_name(name:str):
    splited = name.split("_")
    list_words = []
    for item in splited:
        list_words.append(item.capitalize())
        
    name =" ".join(list_words)
    
    return name