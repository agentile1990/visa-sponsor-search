"""
Abstract base class for all country parsers
"""


class CountryParser():
    def __init__(self, name):
        self.name = name

    def parse(self):
        print("[{}] parse not implemented".format(self.name))
