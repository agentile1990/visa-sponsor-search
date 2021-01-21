FROM python:latest

WORKDIR /app

RUN apt update
RUN apt install -y default-jdk

RUN pip install tabula-py

COPY ./src /app

CMD ["python", "app.py"]
