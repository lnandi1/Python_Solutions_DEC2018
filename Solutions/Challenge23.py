#!/usr/bin/python3
import math

print ("----TURF CALCULATOR----")

#Function to calculate the amount of turf required
def calculate(w,l,r):
    lawnArea=w*l
    bedArea=math.pi*r*r
    turf=lawnArea-bedArea
   
    return turf

#User input of width and length of the lawn and the radius of the bed
def main():
    width=int(input("Enter the width of the lawn: "))
    length=int(input("Enter the length of the lawn: "))
    radius=int(input("Enter the radius of the flower bed: "))

    #Calls the calculate function, passing the width, length and radius variables
    turf_needed = calculate(width,length,radius)
    print("You need",round(turf_needed,2),"square metres of turf")
main()




