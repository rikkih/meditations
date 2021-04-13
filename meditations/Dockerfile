FROM python:3.8-slim

RUN useradd -m -r -u 1000 -U app
USER app
WORKDIR /home/app

COPY ./requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
EXPOSE 5000

CMD ["python", "-m", "flask", "run"]

