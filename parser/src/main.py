"""
Parse visa sponsorship data from sources

This program obtains raw sponsorship data from official sources and
parses this data for insertion into the database. 
"""

import psycopg2
import country_parser
import models


def connect():
    """Returns a connection to the database"""
    conn = psycopg2.connect(
        "host=postgresql dbname=visa_sponsorship_search user=postgres password=example"
    )

    conn.autocommit = True

    return conn


def get_countries(conn):
    """Returns a list of country records from the database"""
    cur = conn.cursor()

    cur.execute("SELECT * FROM countries")
    countries = cur.fetchall()

    return countries


def main():
    # Get connection to database
    conn = connect()

    # Initialize models
    models.initialize(conn)
    Country = models.Country

    for country in Country.list():
        getattr(country_parser, country.code3)(country)


if __name__ == "__main__":
    main()
