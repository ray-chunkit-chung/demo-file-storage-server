# https://hub.docker.com/r/nginx/unit
FROM python:3.11 as build-backend

# Setup nginx config
# https://unit.nginx.org/installation/#docker-image
COPY ./config/config.json /docker-entrypoint.d/config.json

# Copy app files
RUN mkdir -p build/app
COPY ./file_storage_server ./build/app
COPY ./requirements-prod.txt ./build/requirements.txt
COPY ./.env ./build/.env

# Install dependencies and remove unnecessary files
# https://unit.nginx.org/howto/docker/
RUN apt update && apt install -y python3-pip                               \
  && pip3 install -r /build/requirements.txt                               \
  && apt remove -y python3-pip                                             \
  && apt autoremove --purge -y                                             \
  && rm -rf /var/lib/apt/lists/* /etc/apt/sources.list.d/*.list

# listens on port 80
EXPOSE 80

# Spin up server
# docker build . -t raychung/file-storage-server:latest
# docker run --rm -it -p 80:80/tcp raychung/file-storage-server:latest