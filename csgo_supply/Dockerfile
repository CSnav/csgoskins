# syntax=docker/dockerfile:1
FROM python:3.10.7
WORKDIR /csgo_supply
COPY requirements.txt /csgo_supply/
RUN pip install -r requirements.txt
COPY . /csgo_supply/

