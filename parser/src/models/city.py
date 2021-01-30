"""
A model describing city records in the database
"""

from .model import Model


class City():
    def __init__(self, dict):
        self.id = dict["id"]
        self.name = dict["name"]
        self.countryId = dict["countryId"]


class CityModel(Model):
    def __init__(self, conn):
        super().__init__(conn)

    def upsert(self, data):
        self.cur.execute("""
            INSERT INTO "cities" ("name", "countryId") VALUES ('{}', '{}')
            ON CONFLICT ("name", "countryId") DO UPDATE
                SET "id" = "cities"."id"
            RETURNING "id"
        """.format(data["name"], data["countryId"]))
        self.conn.commit()

        return self.find(self.cur.fetchone()[0])

    def find(self, id):
        self.cur.execute("""
            SELECT * FROM "cities" WHERE "id" = '{}'
        """.format(id))

        city = self.cur.fetchone()

        if not city:
            return None
            
        return City({
            "id": city[0],
            "name": city[1],
            "countryId": city[2]
        })
