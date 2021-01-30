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
    return psycopg2.connect(
        "host=postgresql dbname=visa_sponsorship_search user=postgres password=example"
    )


def get_countries(conn):
    """Returns a list of country records from the database"""
    cur = conn.cursor()

    cur.execute("SELECT * FROM countries")
    countries = cur.fetchall()
    cur.close()

    return countries


def main():
    # Get connection to database
    conn = connect()

    # Initialize models
    Country = models.CountryModel(conn)
    City = models.CityModel(conn)
    Company = models.CompanyModel(conn)

    for country in Country.list():
        getattr(country_parser, country.code3)()


if __name__ == "__main__":
    main()
