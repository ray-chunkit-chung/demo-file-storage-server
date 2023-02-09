import os
import shutil
import hashlib
import uvicorn

from glob import glob
from fastapi import FastAPI, File, UploadFile

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, 'local')
if not os.path.exists(UPLOAD_DIR):
    os.mkdir(UPLOAD_DIR)

app = FastAPI()


@app.get('/')
async def hello():
    """
    Minimal get to test the server alive
    """
    return {'message': 'Hello backend'}


@app.post('/files/')
async def upload_file(file: UploadFile | None = None):
    if file:
        filename = file.filename
        fileobj = file.file
        file_path = os.path.join(UPLOAD_DIR, filename)
        with open(file_path, 'wb') as f:
            shutil.copyfileobj(file.file, f)
        return {'filename': filename, 'message': 'file uploaded successfully'}
    return {'message': 'File not found'}


@app.delete('/files/{filename}')
async def delete_file(filename: str | None = None):
    if filename:
        file_path = os.path.join(UPLOAD_DIR, filename)
        if os.path.exists(file_path):
            os.remove(file_path)
            return {'message': 'File deleted successfully'}
    return {'message': 'File not found'}


@app.get('/files')
async def get_files():
    abs_paths = glob(os.path.join(UPLOAD_DIR, '*'))
    rel_paths = [os.path.relpath(p, UPLOAD_DIR) for p in abs_paths]
    return rel_paths


if __name__ == '__main__':
    uvicorn.run('backend:app', port=8000, reload=True)
