"""
A model describing sponsorship records in the database
"""
import hashlib
import json
from titlecase import titlecase
from .model import Model


class Sponsorship():
    def __init__(self, dict):
        self.id = dict["id"]
        self.countryId = dict["countryId"]
        self.cityId = dict["cityId"]
        self.companyId = dict["companyId"]
        self.type = dict["type"]
        self.route = dict["route"]


class SponsorshipModel(Model):
    def __init__(self, conn):
        super().__init__(conn)

    def upsert(self, data):
        self.cur.execute("""
            INSERT INTO "sponsorships" (
                "countryId", 
                "cityId",
                "companyId",
                "type", "route"
            ) VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT ("hash") DO UPDATE
                SET "id" = "sponsorships"."id"
            RETURNING "id"
        """, (
            data["countryId"],
            data["cityId"],
            data["companyId"],
            titlecase(data["type"]),
            titlecase(data["route"])
        ))

        return self.find(self.cur.fetchone()[0])

    def find(self, id):
        self.cur.execute("""
            SELECT * FROM "sponsorships" WHERE "id" = '{}'
        """.format(id))

        sponsorship = self.cur.fetchone()

        if not sponsorship:
            return None

        return Sponsorship({
            "id": sponsorship[0],
            "countryId": sponsorship[1],
            "cityId": sponsorship[2],
            "companyId": sponsorship[3],
            "type": sponsorship[4],
            "route": sponsorship[5],
        })
