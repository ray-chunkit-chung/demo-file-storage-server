# Simple file storage server

This challenge is to create a simple file storage server with a command line interface with the files on the server.

This is a part of the job application process for Woven City.

## Idea or Ingenuity in design

The architecture is designed based on the following principles:

1. Minimal: easy to understand and use by end users
2. Easy to distribute, maintain, and config by ops team members
3. Easy to add/update features by dev team members

### Key considerations

Some key considerations required by the challenge are addressed as follows:

- Provide unit tests to ensure we notice any frontend or backend functionality is broken due to code changes

- Easy-to-use CLI design: fs-store upload-file <i>filename</i>, fs-store delete-file <i>filename</i>, fs-store list-files

- Maintain the project with standard toolings and ensure reproducible builds using, e.g., docker. See Framework and toolkit information below

- Support simple installation methods for easy software distribution: Method (1) from the docker image, Method (2) from the source. See How to build and run (distribute) the code below

### General thought process

To create a simple file storage server with a command line interface, I followed the thought process:

1. Choose a programming language and select the appropriate libraries for file management and command line interface.
2. Implement a server that listens for client requests and provides basic CRUD (create, read, update, delete) operations for files stored on the server.
3. Create a command line interface that communicates with the server using the appropriate protocol (e.g., HTTP or FTP) and allows users to perform operations such as uploading, deleting, and listing files.
4. Test the file storage server thoroughly to ensure that it works as expected and is secure.

From an architectural perspective, the system consists of two parts:

1. Frontend cli app to run cmd of fs-store
2. Backend app with RESTful endpoints to support curl file upload, delete, and lists

## How to build and run (distribute) the code

### Install method 1: from the docker image

Prerequisite: The users' machine can download the docker image and run it in -it mode

Download the image for dev

```bash
docker run --rm -it  raychung/server-dev:python3.11.2-bullseye
```

See Dockerfile in this project

Start backend RESTfull server by

```bash
source ./.venv/bin/activate
python file_storage_server/backend.py
```

A .venv in the image is pre-built for further development. Users can also use requirements.txt to create their dev env.

Please notice that the image is solely for dev purposes. **DO NOT** use in production.

### Install method 2: from source

Prerequisite: Python 3.11.2 and pip are installed in a .venv

```bash
# Install dependencies
source ./.venv/bin/activate   # linux
# .venv\Scripts\activate      # windows
pip install --upgrade -r requirements.txt

# Install fs-store cli (See pyproject.toml & file_storage_server/cli.py)
poetry lock
poetry install

# Spin up the restful backend for the local test (See localhost:8000/docs)
python file_storage_server/backend.py
```

### Usage

After installation, fs-store is available:

```bash
fs-store --help
```

The file storage server cli has three commands:

```bash
fs-store upload-file <filename>
fs-store delete-file <filename>
fs-store list-files
```

They are supported by the corresponding backend services:

1. Upload a file ex. POST /files/ with curl -F 'file=@xxxx.json;type=application/json'
2. Delete a file ex. DELETE /files/{filename} where {filename} is a path parameter
3. List uploaded files (if a file is uploaded then deleted it should not be listed) ex. GET /files may return a list of files: [file1.txt, file2.txt, ..]

## Framework and toolkit information

- fastapi (backend)
- typer (cli frontend)
- poetry (packaging)
- pytest (unit test)
- docker (deploy)

Tools are chosen because they are easy to understand, use, test, and maintain.

App folder structure

```md
root/
├── .vscode
├── file_storage_server
│   ├── __init__.py
│   ├── __main__.py
│   ├── cli.py
│   └── backend.py
├── tests
│   ├── __init__.py
│   ├── test_cli.py
│   └── test_backend.py
├── .env
├── .gitignore
├── Dockerfile
├── LICENSE
├── poetry.lock
├── pyproject.toml
├── README.md
└── requirements.txt
```

## OS and env setting information

Install method 1 prerequisite: Users' machine can download the docker image and run in -it mode.

Install method 2 prerequisite: Python 3.11.2 and pip are installed in a .venv

For both frontend and backend applications, the default setting will be sufficient without any changes. However, users can customize configurations through .env file in the project. In cli.py, the dotenv module will load the .env when fs-store is executed.

## Test code

Two sets of tests are created:

- command line app (tests/test_cli.py)
- backend RESTapi endpoints (tests/test_backend.py)

The tests contain both happy and unhappy paths, e.g., when successful file upload/delete, or when files are not found. They are available below via pytest

```bash
python -m pytest tests
```

#################################################

## Reference

The following websites brought me a lot of insights. I am indebted to the authors for their contributions to knowledge and open source project

<https://fastapi.tiangolo.com/tutorial/first-steps/>

<https://typer.tiangolo.com/tutorial/first-steps/>

<https://pypi.org/project/tornado-file-server/>

<https://github.com/GeekRicardo/image_server>

<https://github.com/GeekRicardo/file-download-server>
