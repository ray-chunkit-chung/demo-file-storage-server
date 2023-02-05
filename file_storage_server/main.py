import typer


app = typer.Typer()


@app.callback()
def callback():
    """
    Hello file storage server
    """


@app.command()
def upload_file():
    """
    upload_file
    """
    typer.echo("upload_file")


@app.command()
def delete_file():
    """
    delete_file
    """
    typer.echo("delete_file")


@app.command()
def list_files():
    """
    list_files
    """
    typer.echo("list_files")
