import random
chars = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
length=int(input("enter length: "))
password=""

for a in range(length):
    password+=random.choice(chars)
    print(password)