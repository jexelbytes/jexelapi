from fastapi import HTTPException

class UnsuportedFileTypeException():
    def __init__(self) -> None:
        raise HTTPException(status_code=400, detail="Supported file types: jpg, jpeg, png")