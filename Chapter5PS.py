# Q:1 Write a program to create a dictionary of Hindi words with values as their english translation. Provide user with an option to look it up!

dictionary = {
    "Namkin": "Salty",
    "Mitha": "Sweet",
    "Pani": "Water",
    "Garm": "Hot",
    "Thanda": "Cold",
}
while True:
    hindi_word = input("Enter a Hindi word (or 'exit' to quit): ")

    if hindi_word == 'exit':
        break

    translation = dictionary.get(hindi_word)
    if translation is not None:
        print(f"The English translation of '{hindi_word}' is '{translation}'.")
    else:
        print(f"'{hindi_word}' not found in the dictionary.")

# Q:2 Write a program to input eight numbers from the user nd display all the unique numbers(once).

numbers = []
for i in range(8):
    num = int(input("Enter a number: "))
    numbers.append(num)
unique_numbers = set(numbers)
print("Unique numbers:", unique_numbers)

# Q:3 Can we have a set with 18(int) and "18"(str) as a values in it?

my_set = {18, "18"}  # This will raise a TypeError

# Q:4 What will be the length of following set S.
# S = set()
# S.add(20)
# S.add(20.0)
# S.add("20") => Length of S after these operations?

S = set()
S.add(20)
S.add(20.0)
S.add("20")
print("Length of S:", len(S)) 

# Q:5 S = {}
# What is the type of S ?

S = set()  # This creates an empty set

# Q:6 Create an empty dictionary. Allow 4 friends to enter their favourite language as values and use keys as their names. Assume that the names are unique. 

favorite_languages = {
    "Friend1": input("Enter Friend1's favorite language: "),
    "Friend2": input("Enter Friend2's favorite language: "),
    "Friend3": input("Enter Friend3's favorite language: "),
    "Friend4": input("Enter Friend4's favorite language: "),
}
print("Favorite languages:", favorite_languages)

# Q:7 If names of 2 friends are same; What will to the program in problem 6 ?

favorite_languages = {
    "Alice": "Python",
    "Bob": "Java",
    "Alice": "C++",  # This will overwrite the previous value for "Alice"
    "David": "JavaScript"
}
print("Favorite languages:", favorite_languages)

# Q:8 If languages of two friends are same; what will happen to the program in problem6 ?

favorite_languages = {}
favorite_languages["Alice"] = "Python"
favorite_languages["Bob"] = "Java"
favorite_languages["Charlie"] = "Python"  # Overwrites the value for "Alice"
favorite_languages["David"] = "JavaScript"
print("Favorite languages:", favorite_languages)

# Q:9 Can you change the values inside a list which is contained in set S
# S={8, 7, 12, "Harry", [1,2]}

'''No, you cannot change the values inside a list that is contained within a set because sets in Python are designed to only store immutable objects. Lists are mutable, meaning their contents can be modified, which makes them ineligible to be stored in a set. If you try to create a set with a mutable object like a list, you will encounter a TypeError'''