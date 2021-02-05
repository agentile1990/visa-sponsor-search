"""
A model describing company records in the database
"""
from titlecase import titlecase

from .model import Model


class Company():
    def __init__(self, dict):
        self.id = dict["id"]
        self.name = dict["name"]
        self.countryId = dict["countryId"]
        self.cityId = dict["cityId"]


class CompanyModel(Model):
    def __init__(self, conn):
        super().__init__(conn)

    def upsert(self, data):
        self.cur.execute("""
            INSERT INTO "companies" ("name", "countryId", "cityId") VALUES (%s, %s, %s)
            ON CONFLICT ("name", "countryId", "cityId") DO UPDATE
                SET "id" = "companies"."id"
            RETURNING "id"
        """, (titlecase(data["name"]), data["countryId"], data["cityId"],)
        )

        return self.find(self.cur.fetchone()[0])

    def find(self, id):
        self.cur.execute("""
            SELECT * FROM "companies" WHERE "id" = %s
        """, (id,))

        company = self.cur.fetchone()
        if not company:
            return None

        return Company({
            "id": company[0],
            "name": company[1],
            "countryId": company[2],
            "cityId": company[3]
        })
