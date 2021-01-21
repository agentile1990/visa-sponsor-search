"""
A class to store information about a sponsorship
"""
class Sponsorship:
    def __init__(self):
        self.type_level = ""
        self.route = ""

    
    def print_sponsorship(self):
        print("\t Type & Level:", self.type_level)
        print("\t Route:", self.route)
        print()
