import random
randNumber = random.randint(1,100)
userGuess = None
guesses = 0

while(userGauss != randNumber):
    userGauss = int(input("Enter your guess: "))
    guesses += 1
    if(userGauss==randNumber):
      print("You guessed it right!")
    else:
        if(userGuess>randNumber):
            print("You guessed it wrong! Enter a smaller number")  
        else:
            print("You guessed it wrong! Enter a larger number")
print(f"You guessed the number in {guesses} guesses")       