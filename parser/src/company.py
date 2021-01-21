from sponsorship import Sponsorship

"""
A class to store information about a company
"""
class Company:
    def __init__(self, name):
        self.name = name
        self.city = ""
        self.sponsorships = []


    def add_sponsorship(self, type_level, route):
        sponsorship = Sponsorship()

        sponsorship.type_level = type_level
        sponsorship.route = route

        self.sponsorships.append(sponsorship)

    
    def print_company(self):
        print("Name: ", self.name)
        print("City:", self.city)
        print("Sponsorships:")

        for sponsorship in self.sponsorships:
            sponsorship.print_sponsorship()

        print()
