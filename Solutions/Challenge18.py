#!/usr/bin/python3

print ("----TIMES TABLE GENERATOR----")

#asks the user to input a number
num=int(input("Enter a number: "))

#this loop generates the times table for the number stored in the num variable
for x in range(1,11):
    print (x*num)
   


input("Press enter to close program")
