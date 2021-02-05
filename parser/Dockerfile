FROM python:latest

WORKDIR /app

RUN apt update
RUN apt install -y ghostscript python3-tk libgl1-mesa-glx

RUN pip install camelot-py[all] psycopg2-binary titlecase

COPY ./src /app

CMD ["python", "main.py"]
