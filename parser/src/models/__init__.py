"""
Model classes describing table records in the database
"""

from .model import Model

from .country import CountryModel
from .city import CityModel
from .company import CompanyModel
from .sponsorship import SponsorshipModel


initialized = False

Country = None
City = None
Company = None
Sponsorship = None


def initialize(conn):
    global initialized
    global models

    if initialized:
        return

    global Country
    Country = CountryModel(conn)

    global City
    City = CityModel(conn)

    global Company
    Company = CompanyModel(conn)

    global Sponsorship
    Sponsorship = SponsorshipModel(conn)

    initialized = True
