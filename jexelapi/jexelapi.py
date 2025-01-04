from sys import argv
from controllers.exceptions.exceptions import InvalidArgumentExecption, RequiredArgumentException
from controllers.modules.basic import create_basic_module
    
def initialize_app():
    
    summary = "summary"
    name = "name"
    description = "description"
    
    for argument in argv:
        if "--summary=" in argument:
            summary = argument.replace("--summary=","")
        elif "--name=" in argument:
            name = argument.replace("--name=","")
        elif "--description=" in argument:
            description = argument.replace("--description=","")
    
    from controllers.init.init import initialize
    initialize(app_name=name, app_summary=summary, app_description=description)

def new_module():
    
    name:str = None
    module_type:str = 'basic' #('basic', 'complex')
    
    for argument in argv:
        
        if "--module_type=" in argument:
            tmp = argument.replace("--module_type=","")
            if tmp not in ('basic', 'complex'):
                raise InvalidArgumentExecption(accepted_arguments=('basic', 'complex'))
            module_type = tmp
            
        elif "--name=" in argument:
            name = argument.replace("--name=","")
    
    if name == None:
        raise RequiredArgumentException(accepted_arguments="name")
        
    if module_type == "basic":
        create_basic_module(name=name)
    elif module_type == "complex":
        print("complex")

for item in argv:
    if item == "init":
        initialize_app()
    elif item == "module":
        new_module()
    elif item == "":
        pass