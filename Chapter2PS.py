# Q:1 Write a python program to add two numbers.

num1 = 1.5
num2 = 6.3
sum = num1 + num2
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

# Q:2 Write a python program to find remaining when a number is divided by 2.

num = int(input("Enter a number: "))
remainder = num % 2
print(f"The remainder when {num} is divided by 2 is: {remainder}")  

# Q:3 Check the type of the variable assigned using input() function.mro

user_input = input("Enter something: ")
print("Type:", type(user_input))


# Q:4 Use comparision operators to find out whether a given variable a is greater than 'b' or not. Take a=34 and b=80.

a = 34
b = 80

if a > b:
    print("a is greater than b")
else:
    print("a is not greater than b")

# Q:5 Write a python program to find average of two numbers entered by the user.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

average = (num1 + num2) / 2

print("The average of", num1, "and", num2, "is:", average)

# Q:6 Write a python program to calculate square of a number entered by the user.

num = float(input("Enter a number: "))
print("The square of", num, "is", num ** 2)