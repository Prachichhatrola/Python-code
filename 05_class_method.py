class Employee:
    company = "Camel"
    salary = 100
    location = "Delhi"\

    def changeSalary(self, sal):
        self.salary = sal    

e = Employee()  
print(e.salary)
e.changeSalary(455)
print(e.salary)
print(Employee.salary)  

