from file_storage_server.main import app, APP_NAME, VERSION

from typer.testing import CliRunner

runner = CliRunner()


def test_version():
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert f"{APP_NAME} v{VERSION}\n" in result.stdout


def test_upload_file():
    pass


def test_delete_file():
    pass


def test_list_files():
    pass
