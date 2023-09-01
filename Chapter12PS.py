# Q:1 Write a program to open three files 1.txt, 2.txt and 3.txt. If any of these files are not present, a message without exiting the program must be printed prompting the same.

file_names = ["1.txt", "2.txt", "3.txt"]

for file_name in file_names:
    try:
        with open(file_name, "r") as file:
            # Perform operations on the file if needed
            print(f"File {file_name} opened successfully.")
    except FileNotFoundError:
        print(f"File {file_name} is not present.")

# Q:2 Write a program to print third, fifth and seventh element from a list using enumerate function.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for index, value in enumerate(my_list):
    if index in (2, 4, 6):
        print(f"Element at index {index}: {value}")

# Q:3 Write a list comprehension to print a list which contains the multiplication table of a user entered number.

# Get the user input for the number
number = int(input("Enter a number: "))

# Use a list comprehension to generate the multiplication table
multiplication_table = [number * i for i in range(1, 11)]

# Print the multiplication table
print(f"Multiplication table for {number}:")
for i, result in enumerate(multiplication_table, start=1):
    print(f"{number} x {i} = {result}")

# Q:4 Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the ZeroDivisionError.

try:
    a = int(input("Enter the numerator (a): "))
    b = int(input("Enter the denominator (b): "))

    result = a / b

    if b == 0:
        raise ZeroDivisionError  # Raise a ZeroDivisionError if b is 0

    print(f"{a}/{b} = {result}")
except ZeroDivisionError:
    print("Division by zero is not allowed. Result is infinite.")
except ValueError:
    print("Invalid input. Please enter integers for both numerator and denominator.")

# Q:5 Store the multiplication tables generated in problem 3 in a file named Tables.txt

# Get the user input for the number
number = int(input("Enter a number:"))

# Use a list comprehension to generate the multiplication table
multiplication_table = [f"{number} x {i} = {number * i}\n" for i in range(1, 11)]

# Define the file name
file_name = "Tables.txt"

# Write the multiplication table to the file
with open(file_name, "w") as file:
    file.writelines(multiplication_table)

print(f"Multiplication table for {number} has been written to {file_name}.")
