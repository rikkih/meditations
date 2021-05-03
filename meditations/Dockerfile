FROM python:3.8-slim

RUN useradd -m -r -u 1000 -U app
USER app
WORKDIR /home/app

COPY . ./meditations
COPY ./migrations ./migrations
RUN pip install --upgrade pip && pip install -r ./meditations/requirements.txt

ENV PATH=/home/app/.local/bin:$PATH
