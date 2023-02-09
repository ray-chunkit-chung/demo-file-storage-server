# File storage server

## Install fs-store file storage server

Prerequsite: Python 3.11.1 installed in .venv

```bash
# Install dependencies
./.venv/bin/activate   # linux
pip install --upgrade -r requirements.txt

# Install fs-store cli (See pyproject.toml & file_storage_server/cli.py)
poetry install

# Spin up restful backend for local test (See localhost:8000/docs)
source .env
python file_storage_server/backend.py
```

## Usage of fs-store file storage server

There are three commands for this file storage server:

```bash
fs-store upload-file <filename>
fs-store delete-file <filename>
fs-store list-files
```

They are supported by the corresponding backend services:

1. Upload a file ex. POST /files/ with curl -F 'file=@xxxx.json;type=application/json'
2. Delete a file ex. DELETE /files/{filename} where {filename} is a path parameter
3. List uploaded files (if a file is uploaded then deleted it should not be listed) ex. GET /files may return a list of files: [file1.txt, file2.txt, ..]

## Architecture principles

1. Minimal: easy to use by end users
2. Easy to distribute, maintain, config by ops team members
3. Easy to add/update features by dev team members

### Tech stack

- fastapi (backend)
- typer (cli)
- poetry (packaging)
- docker (deploy)

### Test cases

Two sets of tests are created:

- command line app (tests/test_cli.py)
- backend RESTapi endpoints (tests/test_backend.py)

The tests contain both happy and unhappy path, e.g., when succesful file upload/delete, or when files are not found.

## What to return back to us

The project folder and all its contents
2. Please provide a complete README file that includes following contents:
a. What is your idea or Ingenuity in design
b. Instructions on how to build and run (distribute) your code
c. framework and tool / kit information if you use
d. Operating system and environment setting information if necessary
3. Make sure your code is well covered by test code to illustrate its robustness.
4. Please zip or tar everything in a directory named yourfirst.lastname/ and return
via email
5. In your email response please let us know roughly how many hours you spent on
this exercise (we will not grade you this on this answer -- it is helpful for us to
normalize the difficulty of challenges)

## Thought process

To create a simple file storage server with a command line interface, you could follow these steps:

1. Choose a programming language and select the appropriate libraries for file management and command line interface.

2. Implement a server that listens for client requests and provides basic CRUD (create, read, update, delete) operations for files stored on the server.

3. Create a command line interface that communicates with the server using the appropriate protocol (e.g., HTTP or FTP) and allows users to perform operations such as uploading, downloading, and deleting files.

4. Store the files on the server's file system in a well-organized manner, with appropriate permissions and backup mechanisms in place.

5. Test the file storage server thoroughly to ensure that it works as expected and is secure.

Some popular programming languages for creating file storage servers include Python, Java, and Ruby. The choice of language and libraries will depend on your specific requirements and constraints.

## Step-by-step doc of creating this file storage server

App folder structure

```md
root/
│
├── file-server/
│   ├── __init__.py
│   ├── __main__.py
│   ├── cli.py
│   ├── config.py
│   ├── database.py
│   └── main.py
│
├── tests/
│   ├── __init__.py
│   └── test_main.py
│
├── pyproject.toml
├── README.md
└── requirements.txt
```

Step 2 Install python 3.11 on debian 11
<https://aruljohn.com/blog/install-python-debian/>

Install python 3.11 for latest typing convention

```bash
# download
cd /tmp/
wget https://www.python.org/ftp/python/3.11.1/Python-3.11.1.tgz
tar -xzvf Python-3.11.1.tgz
cd Python-3.11.1/

# install build tools
sudo apt update
sudo apt install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev

# configure, make and make install. Python3.11 will be in /usr/local/bin/python3.11
./configure --enable-optimizations
make -j `nproc`
sudo make altinstall

# make the default version as Python 3.11.1 
sudo ln -s /usr/local/bin/python
sudo ln -s /usr/local/bin/python3.11 /usr/local/bin/python
```

Create venv for dev

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install --upgrade -r requirements.txt
```

Step 2 Install fs-store

```bash
poetry install 
fs-store --version
```

Step 3 Unit test

```bash
python -m pytest tests/
```

Step 4 Launch file server backend

```bash
uvicorn backend:app --reload
```

### Reference

<https://realpython.com/python-typer-cli/>

<https://typer.tiangolo.com/tutorial/first-steps/>

<https://typer.tiangolo.com/tutorial/package/>

<https://dev.to/meseta/explaining-typer-and-fastapi-dependency-injection-and-rolling-your-own-in-python-2bf2>

<https://pypi.org/project/tornado-file-server/>

<https://github.com/GeekRicardo/image_server>

<https://github.com/GeekRicardo/file-download-server>

<https://learn.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=flask%2Cwindows%2Cazure-cli%2Cvscode-deploy%2Cdeploy-instructions-azportal%2Cterminal-bash%2Cdeploy-instructions-zip-azcli>

<https://docker-fastapi-projects.readthedocs.io/en/latest/nginx.html>

### Docker dev env trouble shoot

If git folder fatal,

```bash
git config --global --add safe.directory /com.docker.devenvironments.code
```
