# syntax=docker/dockerfile:1

FROM python:3.9-slim-buster

WORKDIR /app_wd/

# Copy requirements
COPY requirements.txt requirements.txt
# Install requirements
RUN pip3 install -r requirements.txt

COPY . .

