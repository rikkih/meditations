FROM python:3.8-alpine

RUN groupadd -r app && useradd --no-log-init -r -g app app
USER app

WORKDIR /home/app

COPY ./requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 5000

CMD ["flask", "run"]

