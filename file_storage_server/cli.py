import os
import tomli
import typer
import requests

from typing import Optional


# poetry project attributes
DIRNAME = os.path.join(os.path.dirname(__file__))
TOML_PATH = os.path.join(DIRNAME, '..', 'pyproject.toml')
with open(TOML_PATH, 'rb') as fp:
    poetry_attr = tomli.load(fp)
APP_NAME = poetry_attr['tool']['poetry']['name']
VERSION = poetry_attr['tool']['poetry']['version']
BACKEND_URL = 'http://localhost:8000'

app = typer.Typer()


def _version(value: bool) -> None:
    if value:
        typer.echo(f'{APP_NAME} v{VERSION}')
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        '--version',
        '-v',
        help='Show the application version',
        callback=_version,
        is_eager=True,
    )
) -> None:
    """
    A minimal file storage server
    """


@app.command()
def say_hello():
    """ Minimal get to return 'Hello backend' """
    headers = {'accept': 'application/json'}
    response = requests.get(BACKEND_URL, headers=headers)

    # stdout
    typer.echo(response.status_code)
    typer.echo(response.content)


@app.command()
def upload_file(filename: str):
    """
    upload_file
    """
    try:
        headers = {'accept': 'application/json'}
        files = {'file': open(filename, 'rb')}
        response = requests.post(
            f'{BACKEND_URL}/files/', headers=headers, files=files)

        # stdout
        typer.echo(response.status_code)
        typer.echo(response.content)

    except FileNotFoundError:
        typer.echo({"message": "File not found"})


@app.command()
def delete_file(filename: str):
    """
    delete_file
    """
    headers = {'accept': 'application/json'}
    response = requests.delete(
        f'{BACKEND_URL}/files/{filename}', headers=headers)

    # stdout
    typer.echo(response.status_code)
    typer.echo(response.content)


@app.command()
def list_files():
    """
    list_files
    """
    headers = {'accept': 'application/json'}
    response = requests.get(f'{BACKEND_URL}/files', headers=headers)

    # stdout
    typer.echo(response.status_code)
    typer.echo(response.content)
