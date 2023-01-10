class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

prachisApplication = RailwayForm()
prachisApplication.name = "Prachi"
prachisApplication.train = "Rajdhani Express"
prachisApplication.printData()
    