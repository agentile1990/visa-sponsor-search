FROM python:latest

RUN apt update

RUN apt install -y postgresql-client
RUN pip install psycopg2-binary

WORKDIR /db_deploy

COPY ./db_deploy.py ./db_deploy.py

COPY ./migrations/*.sql ./migrations/
COPY ./triggers/*.sql ./triggers/

COPY ./.pgpass ./.pgpass
RUN chmod 0600 ./.pgpass
ENV PGPASSFILE=/db_deploy/.pgpass

CMD ["python", "./db_deploy.py"]
