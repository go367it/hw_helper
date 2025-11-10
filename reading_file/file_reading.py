import os
from pathlib import Path

def read_file(path : Path) -> dict:

    try:
        file_extension = os.path.splitext( os.path.basename(path) )[-1]
        return {"message": file_extension}

    except FileNotFoundError:
        return {"message" : "File not found!"}
    except Exception as e:
        raise 

