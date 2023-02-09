import os
import requests

from dotenv import load_dotenv
from fastapi.encoders import jsonable_encoder

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
    # Initiate the test materials
    filename = os.path.join(TEST_DIR, 'this_file_exists.txt')
    with open(filename, 'w') as f:
        pass

    # Upload file to storage
    headers = {'accept': 'application/json'}
    files = {'file': open(filename, 'rb')}
    response = requests.post(
        f'{BACKEND_URL}/files/', headers=headers, files=files)

    assert response.status_code == 200
    assert 'success' in jsonable_encoder(response.content)


def test_backend_upload_file_unhappy():
    """
    Unhappy path: Expect FileNotFoundError raised
    """
    try:
        filename = os.path.join(TEST_DIR, 'this_file_does_not_exist.txt')
        headers = {'accept': 'application/json'}
        files = {'file': open(filename, 'rb')}
        response = requests.post(
            f'{BACKEND_URL}/files/', headers=headers, files=files)
        assert False
    except FileNotFoundError:
        assert True


def test_backend_delete_file_happy():
    """
    Happy path: Expect file delete successfully
    """
    # Initiate the test materials
    filename = os.path.join(TEST_DIR, 'this_file_exists.txt')
    with open(filename, 'w') as f:
        pass
    headers = {'accept': 'application/json'}
    files = {'file': open(filename, 'rb')}
    _ = requests.post(
        f'{BACKEND_URL}/files/', headers=headers, files=files)

    # Delete file from storage
    headers = {'accept': 'application/json'}
    response = requests.delete(
        f'{BACKEND_URL}/files/this_file_exists.txt', headers=headers)

    assert response.status_code == 200
    assert 'success' in jsonable_encoder(response.content)


def test_backend_delete_file_unhappy():
    """
    Unhappy path: Expect a "File not found" message
    """
    headers = {'accept': 'application/json'}
    response = requests.delete(
        f'{BACKEND_URL}/files/this_file_does_not_exist.txt', headers=headers)

    assert response.status_code == 200
    assert 'File not found' in jsonable_encoder(response.content)


def test_backend_list_files_happy():
    """
    Happy path: Expect uploaded file{i}.txt to be found in stdout
    """
    # Initiate the test materials
    for i in range(10):
        filename = os.path.join(TEST_DIR, f'file{i}.txt')
        with open(filename, 'w') as f:
            pass
        headers = {'accept': 'application/json'}
        files = {'file': open(filename, 'rb')}
        _ = requests.post(
            f'{BACKEND_URL}/files/', headers=headers, files=files)

    # List files in storage
    headers = {'accept': 'application/json'}
    response = requests.get(f'{BACKEND_URL}/files', headers=headers)
    content = jsonable_encoder(response.content)

    assert response.status_code == 200
    for i in range(10):
        assert f'file{i}.txt' in content
