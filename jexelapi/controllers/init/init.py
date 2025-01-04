from ..utilities import render_file
import shutil

def initialize(app_name:str = "app_name", app_summary:str = "app_summary", app_description:str = "app_description"):

    from_directory = "./controllers/init/layouts/core"
    to_directory = "./src"

    shutil.copytree(from_directory, to_directory)
    
    ctx = {
        "app_name":app_name,
        "app_summary":app_summary,
        "app_description":app_description
    }
    
    render_file(path="./src/config.py", ctx=ctx)    
    render_file(path="./src/auth/controllers/google.py", ctx=ctx)
    
    shutil.copy("./controllers/init/layouts/requirements/requirements.txt", "./")
    shutil.copy("./controllers/init/layouts/requirements/.env.example", "./")
    
    print("Done!")
    