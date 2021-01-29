FROM python:latest

WORKDIR /app

RUN apt update
RUN apt install -y default-jdk

RUN pip install tabula-py
RUN pip install psycopg2-binary

COPY ./src /app

CMD ["python", "main.py"]
