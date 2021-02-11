import os
import psycopg2
import re


def parse_credentials():
    credentials_file = open(".pgpass")
    credentials = credentials_file.readline().split(':')

    return {
        "host": credentials[0],
        "dbname": credentials[2],
        "user": credentials[3],
        "password": credentials[4]
    }


def get_connection(credentials):
    return psycopg2.connect(
        "host={} dbname={} user={} password={}".format(
            credentials["host"],
            credentials["dbname"],
            credentials["user"],
            credentials["password"]
        )
    )


def get_version(conn):
    cur = conn.cursor()

    cur.execute("SELECT MAX(id) FROM versions")
    version = cur.fetchone()[0]

    cur.close()
    return version


def update_version(conn, migration):
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO versions (id, description) VALUES ({}, '{}')".format(
            migration["version"], migration["name"])
    )

    conn.commit()
    cur.close()


def parse_migration_file(f):
    match = re.search('(?!\d{2}_)(\d{4})(?=_\w)', f)

    if (match):
        return {"name": match.string, "version": int(match.group())}


def parse_trigger_file(f):
    match = re.search('^trg_', f)

    if (match):
        return {"name": match.string}

def execute_migration(credentials, migration):
    print("[db_deploy] Running migration", migration["name"])
    cmd = "psql -h {} -d {} -U {} -f ./migrations/{}".format(
        credentials["host"],
        credentials["dbname"],
        credentials["user"],
        migration["name"]
    )
    os.system(cmd)

def execute_trigger(credentials, trigger):
    print("[db_deploy] Running trigger", trigger["name"])
    cmd = "psql -h {} -d {} -U {} -f ./triggers/{}".format(
        credentials["host"],
        credentials["dbname"],
        credentials["user"],
        trigger["name"]
    )
    os.system(cmd)


def main():
    print("[db_deploy] running database deploy")

    credentials = parse_credentials()
    conn = get_connection(credentials)

    current_version = get_version(conn)
    print("[db_deploy] current version", current_version)

    # Run Migrations
    files = os.listdir("./migrations")
    for f in files:
        migration = parse_migration_file(f)

        if (not migration):
            continue

        if int(migration["version"] <= current_version):
            continue

        execute_migration(credentials, migration)
        update_version(conn, migration)

    # Update Triggers
    files = os.listdir("./triggers")
    print(files)
    for f in files:
        trigger = parse_trigger_file(f)

        if (not trigger):
            continue

        execute_trigger(credentials, trigger)

    current_version = get_version(conn)
    conn.close()

    print("[db_deploy] complete! version:", current_version)


if __name__ == "__main__":
    main()
