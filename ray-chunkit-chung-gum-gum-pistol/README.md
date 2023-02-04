# essential poetry

<https://typer.tiangolo.com/tutorial/package/>

<https://pypi.org/project/ray-chunkit-chung-gum-gum-pistol/>

![image](https://user-images.githubusercontent.com/26511618/216767867-50a63a7f-bb39-4020-9227-e6672c454c9a.png)

## Step 1 Init project and dependencies

```bash
poetry new ray-chunkit-chung-gum-gum-pistol
cd ray-chunkit-chung-gum-gum-pistol
poetry add typer[all]
poetry add pytest[all]
```

## Step 2 Define app

Define app path

```toml
[tool.poetry.scripts]
gum = "ray_chunkit_chung_gum_gum_pistol.main:app"
```

Install local

```bash
poetry install
```

Try app local

```bash
gum --help
gum load
gum shoot
```

## Step 2 Distribute app

Build wheel file

```bash
poetry build
```

Test by changing to a new venv and install from local dist

```bash
pip install ray-chunkit-chung-gum-gum-pistol\dist\ray_chunkit_chung_gum_gum_pistol-0.1.0-py3-none-any.whl
```

## Step 3 Upload to pypi

Create PYPI_TOKEN and export to env. Then config pypi-token in poetry. Then publish to pypi

```bash
poetry config pypi-token.pypi $PYPI_TOKEN
poetry publish --build
```

Test by changing to a new venv and install from pypi

```bash
pip install ray-chunkit-chung-gum-gum-pistol
gum --help
```
