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

    # # Initiate the test materials
    # filename = os.path.join(TEST_DIR, 'this_file_exists.txt')
    # with open(filename, 'w') as f:
    #     pass

    # headers = {'accept': 'application/json'}
    # files = {'file': open(filename, 'rb')}
    # response = requests.post(
    #     f'{BACKEND_URL}/files/', headers=headers, files=files)

    # assert response.status_code == 200
    # assert 'uploaded successfully' in response.content


def test_backend_delete_file_happy():
    pass


def test_backend_list_files_happy():
    pass
