#!/usr/bin/python3

print ("----GUESS THE NUMBER----")

guess=0

#Loops until the user guesses the number 7
while guess!=7:
    guess=int(input("Enter your guess: "))
    if guess!=7:
        print("Incorrect... guess again")
        
print ("Well done!")


input("Press enter to close program")
