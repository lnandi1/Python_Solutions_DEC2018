#!/usr/bin/python3

def saveScore(n,s):
    #Opens the file or creates it if it doesn't already exist
    file = open("scores.txt", "a")
    #Records the user's score in the file
    file.write("Name: "+n+", Score: "+str(s)+"\n")
    #Closes the file
    file.close()
    return

print("----MATHS QUIZ----\n")

print("----SCORES----")
#Creates the scores.txt file if it doesn't exist
file = open("scores.txt", "a")
file.close()
#Opens the file in read-only mode
file = open("scores.txt", "r")
#Loop that prints each line from the file to the screen
for line in file:
    print(line)

#Variable setup
name=input("Enter your name: ")
score=0

#Question 1
answer=int(input("What is 3 x 5?: "))
if answer==15:
    score=score+1

#Question 2
answer=int(input("What is 10 + 13?: "))
if answer==23:
    score=score+1

#Question 3
answer=int(input("What is 10 / 2?: "))
if answer==5:
    score=score+1

#Calls the saveScore function and passes the name and score variables
saveScore(name,score)


input("Press enter to close program")