# Q:1 Create two virtual environments, install few packages in the first one. How do you create a similar environment in the second one?

# Q:2 Write a program to input name, marks and phone number of a student and format it using the format function like below:
# "The name of the student is Harry, his marks are 72 and phone number is 99999888"

# Input student information
name = input("Enter the name of the student: ")
marks = input("Enter the marks of the student: ")
phone_number = input("Enter the phone number of the student: ")

# Format the information using the format function
formatted_info = "The name of the student is {}, his marks are {} and phone number is {}".format(name, marks, phone_number)

# Print the formatted information
print(formatted_info)

# Q:3 A list contains the multiplication table of 7. write a program to convert it to a vertical string of same numbers.

# List containing the multiplication table of 7
table_of_7 = [7 * i for i in range(1, 11)]

# Convert the list to a vertical string
vertical_string = '\n'.join(map(str, table_of_7))

# Print the vertical string
print(vertical_string)

# Q:4 Write a program to filter a list of numbers which are divisible by 5.

# Input list of numbers
numbers = [10, 15, 20, 25, 30, 35, 40]

# Use list comprehension to filter numbers divisible by 5
divisible_by_5 = [num for num in numbers if num % 5 == 0]

# Print the result
print("Numbers divisible by 5:", divisible_by_5)

# Q:5 Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce

# Define a function to find the maximum of two numbers
def find_max(x, y):
    return x if x > y else y

# Input list of numbers
numbers = [10, 25, 8, 45, 31, 67, 22]

# Use the reduce function to find the maximum
max_number = reduce(find_max, numbers)

# Print the result
print("Maximum number in the list:", max_number)

# Q:6 Run pip freeze for the system interpretor. table the contents and creat a similar virtualence.

# Q:7 Explore the flask module and create a web server using flask & python.