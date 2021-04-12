FROM python:3.8-alpine

RUN adduser -D docker && chown -R docker /meditations
