class Person:
    country = "India"
    
    def takeBreak(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")        

    def takeBreak(self):
        print("I am an Employee so I am Luckily breathing..")    

class Programmer(Employee):
    company="Fiver"    

    def getSalary(self):
        print(f"No salary to Programmer")

    p = Person()
    e = Employee()
    pr = Programmer()
