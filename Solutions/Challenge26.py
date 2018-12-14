#!/usr/bin/python3

def saveScore(n,s):
    #Opens the file or creates it if it doesn't already exist
    file = open("scores.txt", "a")
    #Records the user's score in the file
    file.write("Name: "+n+", Score: "+str(s)+"\n")
    #Closes the file
    file.close()
    return

print("----MATHS QUIZ----")

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

#Prints the score to the screen
print("Your score is: ",score)

#Calls the saveScore function and passes the name and score variables
saveScore(name,score)



#input("Press enter to close program")
