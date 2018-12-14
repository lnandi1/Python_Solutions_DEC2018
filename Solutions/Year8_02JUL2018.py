# Name Exercise 1
# Write a program which prints Merry Xmas

print("Exercise 1")
print("Merry Christmas ")
print("\n")

# Exercise 2
print("Exercise 2")
print("Merry Xmas\nHappy Easter\nHappy New Year")
print("\n")

# Exercise 3

age = int(input("Enter your age "))
print("Your age is ", age)
print("\n")

# Exercise 4
name = input("Enter your name ")
subject = input("Enter your favourite subject ")
print(name, "'s favourite subject is ", subject)
print("\n")

# Exercise 5
num1 = int(input("Enter a number "))
num2 = int(input("Enter another number "))
num3 = num1/num2
print(num3)
print("\n")

# Exercise 6
a = 10
b = 12
total = a/b
print(total)
print("\n")

# Exercise 7
length = float(input("Enter length in metres "))
width = float(input("Enter width in metres "))
Area = length * width
print("The area is ", Area, " metres squared" )
print("\n")


# Exercise 8
for j in range(1,6):
    print(j)
print("\n")

# Exercise 9
# Increasing by increments of 3
for j in range(1,11,3):
    print(j)
print("\n")


# Exercise 10
for j in range(11,51,11):
    print(j)
print("\n")


# Exercise 11
for j in range(5,1,1):
    print(j)
print("\n")


# Exercise 12
month = input("Enter month ")
if month == "December":
    print("Happy Xmas")
else:
    print("Not Xmas Yet")

print("\n")

# Exercise 13
hours = int(input("How many hours do you spend watching TV each day "))
if hours <= 2:
    print("That should not rot your brain")
elif hours <=4 and hours >2:
    print("You should watch less TV ")
else:
    print("You should get rid of your TV")
print("\n")


# Exercise 14
j = 0
while j < 6:
    print(j)
    j = j+1
print("\n")


# Exercise 15
j = 0
while j < 7:
    print(j)
    j = j+2
print("\n")

j = 5
while j > 0:
    print(j)
    j = j - 1
print("\n")


for j in range(5,1,-1):
    print(j)

print("\n)


# Exercise 16
l = float(input("Enter length"))
w = float(input("Enter width"))
h = float(input("Enter height"))
Volume = (l*h*w)/3
print(Volume)
print("\n")


# Exercise 17
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
print("\n")


















    




















































































