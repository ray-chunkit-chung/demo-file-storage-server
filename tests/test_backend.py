import os
import requests

from dotenv import load_dotenv

# Load typer app and poetry project attributes
BASE_DIR = os.path.join(os.path.dirname(__file__))
load_dotenv(os.path.join(BASE_DIR, '..', '.env'))
BACKEND_URL = os.environ['BACKEND_URL']
TEST_DIR = os.path.join(BASE_DIR, 'local')
if not os.path.exists(TEST_DIR):
    os.mkdir(TEST_DIR)


def test_backend_upload_file_happy():
    """
    Happy path: Expect file upload successfully
    """
    pass


def test_backend_delete_file_happy():
    pass


def test_backend_list_files_happy():
    """
    list_files
    """
    headers = {'accept': 'application/json'}
    response = requests.get(f'{BACKEND_URL}/files', headers=headers)

    assert response.status_code == 200
