FROM python:3.8-slim

RUN useradd -m -r -u 1000 -U app
USER app
WORKDIR /home/app

COPY . ./meditations
RUN pip install --upgrade pip && pip install -r ./meditations/requirements.txt

ENV PATH=/home/app/.local/bin:$PATH

CMD ["flask", "run", "--host", "0.0.0.0"]
