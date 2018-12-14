#!/usr/bin/python3

#Asks the user to input a value and stores it in the time variable
time=int(input("How many hours on average do you spend watching TV each day?: "))

#If statement that outputs different strings depending on the value stored in
#the time variable
if time<2:
    print ("That shouldn’t rot your brain too much")
elif time<4:
    print ("Aren’t you getting square eyes?")
else:
    print ("Fresh air beats channel flicking")
   
   
input("Press enter to close program")        
