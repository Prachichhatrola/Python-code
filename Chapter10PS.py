# Q:1 Create a class programmer for storing information of few programmers working at microsoft.

class Programmer:
    def __init__(self, name, employee_id, job_title, years_of_experience):
        self.name = name
        self.employee_id = employee_id
        self.job_title = job_title
        self.years_of_experience = years_of_experience

# Create instances of Programmer class
programmer1 = Programmer("John Doe", "MS12345", "Software Engineer", 5)
programmer2 = Programmer("Jane Smith", "MS67890", "Data Scientist", 3)

# Access and display information about the programmers
print("Programmer 1 Information:")
print(f"Name: {programmer1.name}")
print(f"Employee ID: {programmer1.employee_id}")
print(f"Job Title: {programmer1.job_title}")
print(f"Years of Experience: {programmer1.years_of_experience}")

print("\nProgrammer 2 Information:")
print(f"Name: {programmer2.name}")
print(f"Employee ID: {programmer2.employee_id}")
print(f"Job Title: {programmer2.job_title}")
print(f"Years of Experience: {programmer2.years_of_experience}")

# Q:2 Write a class calculator capable of finding square, cube and squreroot of a number.

import math

class Calculator:
    def __init__(self, number):
        self.number = number

    def find_square(self):
        return self.number ** 2

    def find_cube(self):
        return self.number ** 3

    def find_square_root(self):
        return math.sqrt(self.number)

# Example usage:
# Create an instance of the Calculator class
calculator = Calculator(9)

# Calculate and display square, cube, and square root
print(f"Number: {calculator.number}")
print(f"Square: {calculator.find_square()}")
print(f"Cube: {calculator.find_cube()}")
print(f"Square Root: {calculator.find_square_root()}")

# Q:3 Create a class with a class attribute a; create an object from it and set a directly using object.a = 0. does this change the class attribute?

class MyClass:
    a = 10  # Class attribute 'a'

# Create an object of MyClass
obj1 = MyClass()

# Set 'a' using the object (creates an instance attribute 'a' for obj1)
obj1.a = 0

# Access class attribute 'a' and instance attribute 'a' for obj1
print("Class attribute 'a':", MyClass.a)
print("Instance attribute 'a' for obj1:", obj1.a)

# Create another object of MyClass
obj2 = MyClass()

# Access class attribute 'a' and instance attribute 'a' for obj2
print("Class attribute 'a':", MyClass.a)
print("Instance attribute 'a' for obj2:", obj2.a)

# Q:4 Add a static method in problem 2 to greet the user with hello.

import math

class Calculator:
    def __init__(self, number):
        self.number = number

    def find_square(self):
        return self.number ** 2

    def find_cube(self):
        return self.number ** 3

    def find_square_root(self):
        return math.sqrt(self.number)

    @staticmethod
    def greet_user():
        print("Hello!")

# Create an instance of Calculator class
calculator = Calculator(9)

# Calculate and display square, cube, and square root
print(f"Number: {calculator.number}")
print(f"Square: {calculator.find_square()}")
print(f"Cube: {calculator.find_cube()}")
print(f"Square Root: {calculator.find_square_root()}")

# Call the static method to greet the user
Calculator.greet_user()

# Q:5 Write a class train which has methods to book a ticket, get status (no of seats) and get fare information of trains running under indian railways.

class Train:
    def __init__(self, train_name, total_seats, fare_per_seat):
        self.train_name = train_name
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.fare_per_seat = fare_per_seat

    def book_ticket(self, num_tickets):
        if num_tickets <= self.available_seats:
            self.available_seats -= num_tickets
            return f"Booked {num_tickets} ticket(s) for {self.train_name}."
        else:
            return f"Sorry, not enough seats available on {self.train_name}."

    def get_status(self):
        return f"Available Seats on {self.train_name}: {self.available_seats}/{self.total_seats}"

    def get_fare_info(self, num_tickets):
        total_fare = num_tickets * self.fare_per_seat
        return f"Fare for {num_tickets} ticket(s) on {self.train_name}: {total_fare}"

# Example usage:
train1 = Train("Rajdhani Express", total_seats=200, fare_per_seat=1500)

print(train1.book_ticket(5))  # Book 5 tickets on Rajdhani Express
print(train1.get_status())    # Get status of Rajdhani Express
print(train1.get_fare_info(2))  # Get fare info for 2 tickets on Rajdhani Express

# Q:6 Can you change the self parameter inside a class to something else(say 'harry'). try chaanging self to 'slf' or 'harry' and see the effects.

class MyClass:
    def __init__(slf, value):
        slf.value = value

    def display_value(slf):
        print(slf.value)

obj = MyClass(42)
obj.display_value()
