# Dev only. DO NOT use this image in production
FROM python:3.11.2-bullseye

# Copy project files
RUN mkdir /project
COPY . /project
WORKDIR /project

# Prepare dev env
RUN python -m venv .venv && \
    . .venv/bin/activate && \
    pip install --upgrade -r requirements.txt && \
    poetry lock && \
    poetry install

# Start dev env
ENTRYPOINT [ "/bin/bash" ]
