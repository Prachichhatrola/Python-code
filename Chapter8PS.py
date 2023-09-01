# Q:1 Write  program using function to find greatest of three numbers.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
greatest = max(num1, num2, num3)
print(f"The greatest number among {num1}, {num2}, and {num3} is: {greatest}")

# Q:2 Write a python program using function to convert celsius to fahrenheit.

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")

# Q:3 How do you prevent a python print() function to print a new line at the end.

print("This will print without a newline at the end.", end="")
print("This will be on the same line.")

# Q:4 Write a recursive function to calculate the sum of first n natural numbers.

def sum_of_natural_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_of_natural_numbers(n - 1)
n = int(input("Enter a positive integer n: "))
result = sum_of_natural_numbers(n)
print(f"The sum of the first {n} natural numbers is: {result}")

# Q:5 Write a python function to print first n lines on the following pattern:
#     * * *
#     * *
#     *          for n=3

def print_pattern(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()  
n = int(input("Enter the number of lines (n): "))
print_pattern(n)

# Q:6 Write a python function which converts inches to cms.

def inches_to_cm(inches):
    conversion_factor = 2.54
    centimeters = inches * conversion_factor
    return centimeters
inches = float(input("Enter length in inches: "))
centimeters = inches_to_cm(inches)
print(f"{inches} inches is equal to {centimeters} centimeters.")

# Q:7 Write a python function to remove a given word from a list and strip it at the same time.

def remove_and_strip(word_to_remove, word_list):
    cleaned_list = [word.strip() for word in word_list if word.strip() != word_to_remove]
    return cleaned_list

# Q:8 Write a python function to print multiplication table of a given number.

def print_multiplication_table(number):
    for i in range(1, 11):  
        product = number * i
        print(f"{number} x {i} = {product}")
number = int(input("Enter a number: "))
print_multiplication_table(number)
