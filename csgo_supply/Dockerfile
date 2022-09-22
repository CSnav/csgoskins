# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /csgo_supply
COPY requirements.txt /csgo_supply/
RUN pip install -r requirements.txt
COPY . /csgo_supply/

