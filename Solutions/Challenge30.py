
#Function that can be used to ask each question
def ask(q,s):
    answer=int(input(questions[0][q]))
    if answer==questions[1][q]:
        s=s+1
    return s

print("----MATHS QUIZ----\n")

print("----SCORES----")
#Creates the scores.txt file if it doesn't exist
file = open("test 20th March.txt", "a")
file.close()
#Opens the file in read-only mode
file = open("test 20th March.txt", "r")
#Loop that prints each line from the file to the screen
for line in file:
    print(line)
file.close()

#Variable setup
name=input("Enter your name: ")
score=0
questions=[["What is 3 x 5?: ", "What is 10 + 13?: ", "What is 10 / 2?: "],[15,23,5]]           

#Loop to call ask function to ask each question
for i in range(len(questions)+1):
    score=ask(i,score)


def saveScore(n,s):
    #Opens the file or creates it if it doesn't already exist
    file = open("scores.txt", "a")
    #Records the user's score in the file
    file.write("Name: "+n+", Score: "+str(s)+"\n")
    #Closes the file
    file.close()
    return       

saveScore(name,score)


