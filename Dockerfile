FROM jupyter/datascience-notebook:latest

COPY ./ /home/app

WORKDIR /home/app

RUN pip install -r ./requirements.txt