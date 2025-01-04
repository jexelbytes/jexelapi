
class InvalidArgumentExecption(Exception):
    def __init__(self, accepted_arguments:any):
        print(f"Invalid arguments. accepted={accepted_arguments}")
        
        
class RequiredArgumentException(Exception):
    def __init__(self, accepted_arguments:any):
        print(f"Required argument. detail={accepted_arguments}")