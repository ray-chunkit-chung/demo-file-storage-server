import os
import shutil

from typer.testing import CliRunner
from fastapi.encoders import jsonable_encoder
from file_storage_server.cli import app, APP_NAME, VERSION

# Common path for the cli app tests
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DIR = os.path.join(BASE_DIR, 'local')
if not os.path.exists(TEST_DIR):
    os.mkdir(TEST_DIR)

runner = CliRunner()


def test_cli_version():
    result = runner.invoke(app, ['--version'])
    assert result.exit_code == 0
    assert f'{APP_NAME} v{VERSION}\n' in result.stdout


def test_cli_upload_file_happy():
    """
    Happy path: Expect file upload successfully
    """
    # Initiate the test materials
    test_file_path = os.path.join(TEST_DIR, 'this_file_exists.txt')
    with open(test_file_path, 'w') as f:
        pass

    # Upload test file to storage
    result = runner.invoke(app, ['upload-file', test_file_path])
    assert result.exit_code == 0
    assert 'uploaded successfully' in result.stdout


def test_cli_upload_file_unhappy():
    """
    Unhappy path: Expect a "File not found" message
    """
    result = runner.invoke(
        app, ['upload-file', 'this_file_does_not_exist.txt'])
    assert result.exit_code == 0
    assert 'File not found' in result.stdout


def test_cli_delete_file_happy():
    """
    Happy path: Expect file delete successfully
    """
    # Initiate the test materials
    test_file_path = os.path.join(TEST_DIR, 'this_file_exists.txt')
    with open(test_file_path, 'w') as f:
        pass
    _ = runner.invoke(app, ['upload-file', test_file_path])

    # Delete test file from storage
    result = runner.invoke(app, ['delete-file', 'this_file_exists.txt'])
    assert result.exit_code == 0
    assert 'deleted successfully' in result.stdout


def test_cli_delete_file_unhappy():
    """
    Unhappy path: Expect a "File not found" message
    """
    result = runner.invoke(
        app, ['delete-file', 'this_file_does_not_exist.txt'])
    assert result.exit_code == 0
    assert 'File not found' in result.stdout


def test_cli_list_files_happy():
    """
    Happy path: Expect uploaded file{i}.txt to be found in stdout
    """
    # Initiate the test materials
    for i in range(10):
        filename = os.path.join(TEST_DIR, f'file{i}.txt')
        with open(filename, 'w') as f:
            pass
        _ = runner.invoke(app, ['upload-file', filename])

    # List test files in storage
    result = runner.invoke(app, ['list-files'])
    assert result.exit_code == 0
    for i in range(10):
        assert f'file{i}.txt' in result.stdout


def test_cli_list_files_will_not_show_deleted():
    """
    Happy path: Expect deleted file{i}.txt will not show in stdout
    """
    # Initiate the test materials and upload to storage
    for i in range(10):
        filename = os.path.join(TEST_DIR, f'file{i}.txt')
        with open(filename, 'w') as f:
            pass
        _ = runner.invoke(app, ['upload-file', filename])

    # Delete file1.txt from storage
    _ = runner.invoke(app, ['delete-file', 'file1.txt'])

    # List test files in storage. file1.txt should not show
    result = runner.invoke(app, ['list-files'])
    assert result.exit_code == 0
    for i in range(10):
        if i == 1:
            assert 'file1.txt' not in result.stdout
        else:
            assert f'file{i}.txt' in result.stdout
