FROM debian:bullseye-slim

WORKDIR /app

RUN apt-get update -y && apt-get install -y \
    python3 python3-pip python3-setuptools git

COPY ./requirements.txt /app

COPY ./requirements_dev.txt /app

COPY ./docker-entrypoint.sh /app

RUN chmod +x ./docker-entrypoint.sh

RUN pip install -r ./requirements.txt

RUN pip install -r ./requirements_dev.txt

CMD [ "./docker-entrypoint.sh" ]