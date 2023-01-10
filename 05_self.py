class Employee:
     company = "Google"
     def getSalary():
        print("Salary is 100k")

harry = Employee
harry.getSalary() 
# Employee.getSalary(harry)       