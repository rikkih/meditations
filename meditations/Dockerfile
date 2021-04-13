FROM python:3.8-slim

RUN useradd -m -r -u 1000 -U app
USER app
WORKDIR /home/app

COPY . ./meditations
RUN pip install --upgrade pip && pip install -r ./meditations/requirements.txt

ENV FLASK_APP=meditations
ENV PATH=/home/app/.local/bin:$PATH

RUN ls
RUN pwd

CMD ["python", "__init__.py"]
