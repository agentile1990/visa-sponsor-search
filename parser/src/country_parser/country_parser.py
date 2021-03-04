"""
Abstract base class for all country parsers
"""

import models


class CountryParser():
    def __init__(self, name):
        self.name = name

        self.city_model = models.City

        self.company_model = models.Company

        self.sponsorship_model = models.Sponsorship

    def parse(self):
        print("[{}] parse not implemented".format(self.name))

    def upsertSponsorship(self, data):
        self.sponsorship_model.upsert(data)
