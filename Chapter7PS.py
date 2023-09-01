# Q:1 Write  program to print multiplication table of a given number using for loop.

number = int(input("Enter a number: "))
print(f"Multiplication table for {number}:")
for i in range(1, 11):  
    product = number * i
    print(f"{number} x {i} = {product}")

# Q:2 Write a program to greet all the person names stored in a list l1 and which starts with S.
# l1 = ["Harry", "Soham", "Sachin", "Rahul"]

l1 = ["Harry", "Soham", "Sachin", "Rahul"]
for name in l1:
    if name.startswith("S"):
        print(f"Hello, {name}!")

# Q:3 Attempt problem 1 using while loop.

number = int(input("Enter a number: "))
i = 1
print(f"Multiplication table for {number}:")
while i <= 10:  
    product = number * i
    print(f"{number} x {i} = {product}")
    i += 1

# Q:4 Write a program to find whether a given number is prime or not.

num = int(input("Enter a number: "))
if num < 2:
    is_prime = False
else:
    is_prime = True
for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break
if is_prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

# Q:5 Write a program to find the sum of first n natural numbers using while loop.

n = int(input("Enter a positive integer n: "))
sum_of_natural_numbers = 0
count = 1
while count <= n:
    sum_of_natural_numbers += count
    count += 1
print("The sum of the first", n, "natural numbers is:", sum_of_natural_numbers)

# Q:6 Write a program to calculate the factorial of a given number using for loop.

num = int(input("Enter a non-negative integer: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"The factorial of {num} is {factorial}")

# Q:7 Write a program to print the following star pattern.
#       *
#      ***
#     *****     for n=3

n = 3  # You can change this value to adjust the number of rows

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

# Q:8 Write a program to print the following star pattern:
#    *
#    **
#    ***     for n=3

n = 3  
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()  

# Q:9 Write a program to print the following star.
#     * * *
#     *   *       for n=3
#     * * *

n = 3  
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 1 or i == n or j == 1 or j == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()  

# Q:10 Write a program to print multiplication table n using for loop in reversed order.

n = int(input("Enter a number: "))
print(f"Reversed multiplication table for {n}:")
for i in range(10, 0, -1):  
    product = n * i
    print(f"{n} x {i} = {product}")
