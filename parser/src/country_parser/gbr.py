"""
GBR - Parser for Great Britain / United Kingdom
"""

import camelot
import os
from pathlib import Path

from .country_parser import CountryParser


class GBR(CountryParser):
    def __init__(self, country):
        super().__init__('GBR')

        self.country = country

        self.parse()

    def parse(self):
        # TODO: Need to fetch this from the Home Office
        path = os.path.abspath(os.path.join(
            os.getcwd(), "./localData/test.pdf"))
        print("[GBR] parsing from source:", path)

        # Read first page (adjusted bounds)
        first_table = tables = camelot.read_pdf(
            path,
            pages="1",
            flavor="stream",
            table_regions=["29, 390, 805, 40"]
        )

        # Read all pages
        tables = camelot.read_pdf(
            path,
            pages="all",
            flavor="stream",
            table_regions=["40, 500, 1140, 45"]
        )

        # Replace first page
        tables[0].df = first_table[0].df

        print("[GBR] upserting data")
        company = None
        for table in tables:
            index = 0
            for row in table.df.itertuples():
                try:
                    if row._1:
                        # Company Row
                        city = self.city_model.upsert({
                            "name": row._2,
                            "countryId": self.country.id
                        })

                        company = self.company_model.upsert({
                            "name": row._1,
                            "countryId": self.country.id,
                            "cityId": city.id
                        })
                    else:
                        # Sponsorship Row
                        self.upsertSponsorship({
                            "type": row[len(row) - 2],
                            "route": row[len(row) - 1],
                            "companyId": company.id,
                            "cityId": company.cityId,
                            "countryId": self.country.id
                        })
                    index += 1
                except Exception as e:
                    print("[GBR] Parse Exception:", e)
                    print("[GBR] row:", row)

    def upsertSponsorship(self, data):
        if not data["type"] or not data["route"]:
            raise Exception('GBR sponsorship requires type and route')

        self.sponsorship_model.upsert(data)
