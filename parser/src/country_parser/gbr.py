"""
GBR - Parser for Great Britain / United Kingdom
"""

from .country_parser import CountryParser


class GBR(CountryParser):
    def __init__(self):
        super().__init__('GBR')
        print("[{}] starting".format(self.name))
