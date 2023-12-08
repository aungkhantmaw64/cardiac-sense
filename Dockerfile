FROM debian:bullseye-slim

WORKDIR /app

RUN apt-get update -y && apt-get install -y \
    python3 python3-pip python3-setuptools git

COPY ./requirements.txt /app

RUN pip install -r ./requirements.txt

COPY ./docker-entrypoint.sh /app

ENTRYPOINT [ "/app/docker-entrypoint.sh" ]