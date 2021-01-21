import tabula
from company import Company

class Parser:
    def __init__(self):
        self.companies = [] 

        # Read source file
        self.df = tabula.read_pdf("./localData/2021-01-15_Tier_2_5_Register_of_Sponsors.pdf", pages="1")

        self.run()

    
    def run(self):
        # Loop through rows of source file data
        for i, row in self.df[0].iterrows():
            self.parse_row(row)

        for company in self.companies:
            company.print_company()


    def parse_row(self, row):
        # Get value from 'Organisation Name' column
        #
        # Companies can take up more than one row on the table. This column contains 
        # the company name for the first row of data. Subsequent rows, it evaluates 
        # to 'NaN'
        company_name = row["Organisation Name"]

        if isinstance(company_name, str):
            # Start new company object
            company = Company(company_name)
            company.city = row["Town/City"]

            self.companies.append(company)
        else:
            # Add sponsorship data to the last company object created
            #
            # Sponsorship data is stored on subsequent rows of the company data
            self.companies[len(self.companies) - 1].add_sponsorship(
                row["Type & Rating"],
                row["Route"]
            );


def main():
    Parser()


if __name__ == "__main__":
    main()
