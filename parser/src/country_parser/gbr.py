"""
GBR - Parser for Great Britain / United Kingdom
"""

import camelot
import os
from pathlib import Path

from .country_parser import CountryParser

import models
City = None
Company = None
Sponsorship = None


class GBR(CountryParser):
    def __init__(self, country):
        super().__init__('GBR')

        self.country = country

        global City
        City = models.City

        global Company
        Company = models.Company

        global Sponsorship
        Sponsorship = models.Sponsorship

        self.parse()

    def parse(self):
        # TODO: Need to fetch this from the Home Office
        path = os.path.abspath(os.path.join(
            os.getcwd(), "./localData/2021-01-29_Tier_2_5_Register_of_Sponsors.pdf"))
        print("[GBR] parsing from source:", path)

        # Read first page (adjusted bounds)
        first_table = tables = camelot.read_pdf(
            path,
            pages="1",
            flavor="stream",
            table_areas=["29, 400, 805, 40"]
        )

        # Read all pages
        tables = camelot.read_pdf(
            path,
            pages="all",
            flavor="stream"
        )

        # Replace first page
        tables[0].df = first_table[0].df

        print("[GBR] upserting data")
        company = None
        for table in tables:
            index = 0
            for row in table.df.itertuples():
                try:
                    # Drop header row
                    if index == 0:
                        index += 1
                        continue

                    if row._1:
                        # Company Row
                        city = City.upsert({
                            "name": row._2,
                            "countryId": self.country.id
                        })

                        company = Company.upsert({
                            "name": row._1,
                            "countryId": self.country.id,
                            "cityId": city.id
                        })
                    else:
                        # Sponsorship Row
                        Sponsorship.upsert({
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
