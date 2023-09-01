# Q:1 Write a program to find greatest of four numbers entered by the user.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
num4 = float(input("Enter the fourth number: "))
greatest = max(num1, num2, num3, num4)
print("The greatest number is:", greatest)

# Q:2 Write a program to find out whether a student is pass or fail, if it requires total 40% and at least 33% in each subject to pass. Assume 3 subjects and take as an input from the user.

subject1 = float(input("Enter marks for subject 1: "))
subject2 = float(input("Enter marks for subject 2: "))
subject3 = float(input("Enter marks for subject 3: "))
total_marks = subject1 + subject2 + subject3
percentage = (total_marks / 300) * 100 
if percentage >= 40 and subject1 >= 33 and subject2 >= 33 and subject3 >= 33:
    result = "Pass"
else:
    result = "Fail"
print("Result: {}".format(result))

# Q:3 A spam comment is definded as a text containing following keywords:
# "make a lot of money","Subscribe this", "Click this". write a program to detect these spams.

spam_keywords = ["make a lot of money", "Subscribe this", "Click this"]
comment = input("Enter your comment: ")
comment = comment.lower()
is_spam = any(keyword in comment for keyword in spam_keywords)
if is_spam:
    print("This is a spam comment.")
else:
    print("This is not a spam comment.")

# Q:4 Write a program to find whether a given username contains less than 10 characters or not.

username = input("Enter your username: ")
if len(username) < 10:
    print("The username contains less than 10 characters.")
else:
    print("The username contains 10 or more characters.")

# Q:5 Write a program which finds out whether a given name is present in a list or not.

names = ["Alice", "Bob", "Charlie", "David", "Eva"]
name_to_find = input("Enter a name to search for: ")
if name_to_find in names:
    print(f"{name_to_find} is present in the list.")
else:
    print(f"{name_to_find} is not present in the list.")

# Q:6 Write a program to calculate the grade of a student from his marks from the following scheme:
# 90-100 : Ex
# 80-90 : A
# 70-80 : B
# 60-70 : C
# 50-60 : D
# <50 : F

marks = float(input("Enter the student's marks: "))
if 90 <= marks <= 100:
    grade = "Ex"
elif 80 <= marks < 90:
    grade = "A"
elif 70 <= marks < 80:
    grade = "B"
elif 60 <= marks < 70:
    grade = "C"
elif 50 <= marks < 60:
    grade = "D"
else:
    grade = "F"
print(f"The student's grade is: {grade}")

# Q:7 Write a program to find out whether a given post is talking aout "Harry" or not.

post = input("Enter a post: ")
post = post.lower()
if "harry" in post:
    print("The post mentions 'Harry'.")
else:
    print("The post does not mention 'Harry'.")
