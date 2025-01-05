from ..utilities import render_file, savefile
from ..init.data import requirements, env, alembic_init, ALEMBIC_README, ALEMBIC_SCRIPT
import shutil
import os

def initialize(app_name:str = "app_name", app_summary:str = "app_summary", app_description:str = "app_description"):

    realpath = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")

    from_directory = f"{realpath}/layouts/core"
    to_directory = "./src"

    shutil.copytree(from_directory, to_directory)
    
    ctx = {
        "app_name":app_name,
        "app_summary":app_summary,
        "app_description":app_description
    }
    
    render_file(path="./src/config.py", ctx=ctx)    
    render_file(path="./src/auth/controllers/google.py", ctx=ctx)
    
    savefile("./requirements.txt", text=requirements)
    savefile(".env.example", text=env)
    savefile("./src/alembic.ini", text=alembic_init)
    savefile("./src/migrations/README", text=ALEMBIC_README)
    savefile("./src/migrations/script.py.mako", text=ALEMBIC_SCRIPT)
    
    print("Done!")
    