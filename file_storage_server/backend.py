import os
import shutil
import uvicorn

from glob import glob
from dotenv import load_dotenv
from fastapi import FastAPI, File, UploadFile
from typing import Union

# Common path for the backend app
BASE_DIR = os.path.join(os.path.dirname(__file__))
load_dotenv(os.path.join(BASE_DIR, '..', '.env'))
BACKEND_URL = os.environ['BACKEND_URL']

STORAGE_DIR = os.path.join(BASE_DIR, 'local')
if not os.path.exists(STORAGE_DIR):
    os.mkdir(STORAGE_DIR)

app = FastAPI()


@app.get('/')
async def hello():
    """
    Minimal get to test the server availability
    """
    return {'message': 'Hello backend'}


@app.post('/files/')
async def upload_file(file: Union[UploadFile, None] = None):
    """
    Upload a file to storage directory

    Args:
        file (UploadFile) : Accept, e.g., curl -F 'file=@openapi.json;type=application/json' or form submit

    Returns:
        (dict) : {'message': <result of the request>}

    Raises:
        Exception: If anything unexpected happens
    """
    if file:
        filename = file.filename
        fileobj = file.file
        file_path = os.path.join(STORAGE_DIR, filename)
        with open(file_path, 'wb') as f:
            shutil.copyfileobj(file.file, f)
        return {'message': f'File {filename} uploaded successfully'}
    return {'message': 'File not found'}


@app.delete('/files/{filename}')
async def delete_file(filename: Union[str, None] = None):
    """
    Delete a file from storage directory

    Args:
        filename (str) : Accept url path parameter <BACKEND_URL>/files/<filename>

    Returns:
        (dict) : {'message': <result of the request>}

    Raises:
        Exception: If anything unexpected happens
    """
    if filename:
        file_path = os.path.join(STORAGE_DIR, filename)
        if os.path.exists(file_path):
            os.remove(file_path)
            return {'message': f'File {filename} deleted successfully'}
    return {'message': 'File not found'}


@app.get('/files')
async def get_files():
    """List al files exists in storage directory

    Returns:
       rel_paths (list[str]) : [file1.txt, file2.txt, ...]

    Raises:
        Exception: If anything unexpected happens
    """
    abs_paths = glob(os.path.join(STORAGE_DIR, '*'))
    rel_paths = [os.path.relpath(p, STORAGE_DIR) for p in abs_paths]
    return rel_paths


if __name__ == '__main__':

    # Dev only
    uvicorn.run('backend:app', port=8000, reload=True)
