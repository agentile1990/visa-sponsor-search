"""
A model describing country records in the database
"""

from .model import Model


class Country():
    def __init__(self, dict):
        self.id = dict["id"]
        self.name = dict["name"]
        self.code3 = dict["code3"]


class CountryModel(Model):
    def __init__(self, conn):
        super().__init__(conn)

    def list(self):
        self.cur.execute("SELECT * FROM countries")
        records = self.cur.fetchall()

        countries = []
        for col in records:
            countries.append(
                Country({
                    "id": col[0],
                    "name": col[1],
                    "code3": col[2]
                })
            )

        return countries
