# Q:1 Write a program to store seven fruits in a list entered by the user.

fruits = []
for i in range(7):
    fruits.append(input("Enter a fruit: "))
print("List of fruits:", fruits)

# Q:2 Write a program to accept marks of 6 students and display them in a sorted manner.

marks = []
for i in range(6):
    mark = float(input("Enter the marks of student {}: ".format(i + 1)))
    marks.append(mark)
marks.sort()
print("Marks of 6 students in sorted manner:", marks)

# Q:3 Check that a tuple cannot be changed in python.

my_tuple = (1, 2, "hello", (3, 4))
# Trying to change an element of the tuple will result in an error
# For example, the following line will raise an error:
# my_tuple[0] = 5

# Q:4 Write a program to sum a list with 4 number.

numbers = []
for i in range(4):
    num = float(input("Enter number {}: ".format(i + 1)))
    numbers.append(num)
total_sum = sum(numbers)
print("Sum of the numbers:", total_sum)

# Q:5 Write a program to count the number of zeros in the following tuple:
# a=(7,0,8,0,0,9)

a = (7, 0, 8, 0, 0, 9)
zero_count = a.count(0)
print("Number of zeros in the tuple:", zero_count)
