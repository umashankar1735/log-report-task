FROM python:3.13-slim-bookworm@sha256:56249d7a2f93306106f6d8bcdf6423afb73c1b747d874febcc778beee25cb8bb

RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

WORKDIR /app

COPY access.log /app/access.log