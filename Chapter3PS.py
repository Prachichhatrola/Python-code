# Q:1 Write a python program to display a user entered name followed by Good Afternoon using input() function.

name = input("Enter your name: ")
print("Good Afternoon,", name)

# Q:2 Write a program to fill in a letter template given below with name and date.
# letter = '''Dear <|NAME|>,
#              You are selected!
#              <|DATE|>'''

name = input("Enter your name: ")
date = input("Enter the date: ")

letter_template = '''Dear {},
             You are selected on {}!
            '''.format(name, date)

print(letter_template)


# Q:3 Write a program to detect double spaces in a string.

input_string = input("Enter a string: ")

if "  " in input_string:
    print("Double spaces detected.")
else:
    print("No double spaces found.")


# Q:4 Replace the double spaces from problem 3 with single spaces.

input_string = input("Enter a string: ")

new_string = input_string.replace("  ", " ")

print("Modified string:", new_string)


# Q:5 Write a program to format the following letter using escape sequence charecter. 
# letter = "Dear Harry, This Python course is nice. Thanks!"

letter = "Dear Harry,\n\tThis Python course is nice.\nThanks!"
print(letter)
