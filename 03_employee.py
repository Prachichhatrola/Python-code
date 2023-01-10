class Employee:
    company = "Google"
    salary = 100

prachi = Employee()
harry = Employee()
prachi.salary = 300
harry.salary = 400

print(prachi.company)
print(harry.company)   
Employee.company = "YouTube"
print(prachi.company)
print(harry.company) 
print(prachi.salary)
print(harry.salary)