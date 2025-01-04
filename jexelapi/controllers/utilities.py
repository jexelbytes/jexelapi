from jinja2 import Environment, FileSystemLoader
import subprocess

def run_cmd(command:str):
    str_arguments = ""
    CMD = command
    p = subprocess.Popen(CMD, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    str_arguments = p.stdout.read()
    try:
        str_arguments = f"{str_arguments.decode('ascii')}\n"
    except:
        str_arguments = f"{str_arguments.decode('utf-8')}\n"
    
    return str_arguments

def render_file(path:str, ctx:dict):
    
    filename = path.split("/")[-1]
    
    env = Environment(loader=FileSystemLoader(path.replace(filename,"")))
    template = env.get_template(filename)
    output_from_parsed_template = template.render(ctx)

    with open(path, "w") as fh:
        fh.write(output_from_parsed_template)
        

def openfile(path:str) -> str:
    
    with open(path, 'rt') as f:
        content = f.read()
    
    return content

def savefile(path:str, text:str):
    
    with open(path, 'wt') as f:
        f.write(text)

def appendtextfile(path:str, text:str):
    
    with open(path, 'at') as f:
        f.write(text)