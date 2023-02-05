from file_storage_server.cli import app, APP_NAME, VERSION

from typer.testing import CliRunner

runner = CliRunner()


def test_cli_version():
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert f"{APP_NAME} v{VERSION}\n" in result.stdout


def test_cli_upload_file():
    pass


def test_cli_delete_file():
    pass


def test_cli_list_files():
    pass
