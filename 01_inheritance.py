class Employee:
    company = "Google"
   
    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):
    langauge = "Python"
    company = "YouYube"

    def getLangauge(self):
        print(f"The langauge is {self.langauge}")

    def showDetails(self):
        print("This is a programmer")


e = Employee()
e.showDetails()   
p = Programmer()
p.showDetails() 
# print(p.company)           