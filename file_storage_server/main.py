import os
import tomli
import typer
from typing import Optional


# poetry project attributes
DIRNAME = os.path.join(os.path.dirname(__file__))
TOML_PATH = os.path.join(DIRNAME, '..', 'pyproject.toml')
with open(TOML_PATH, 'rb') as fp:
    poetry_attr = tomli.load(fp)
# COMMAND = next(iter(poetry_attr['tool']['poetry']['scripts']))
APP_NAME = poetry_attr['tool']['poetry']['name']
VERSION = poetry_attr['tool']['poetry']['version']


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
def upload_file():
    """
    upload_file
    """
    typer.echo('upload_file')


@app.command()
def delete_file():
    """
    delete_file
    """
    typer.echo('delete_file')


@app.command()
def list_files():
    """
    list_files
    """
    typer.echo('list_files')

