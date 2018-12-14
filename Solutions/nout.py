#!/usr/bin/python3

#Function to draw a line of the image
def drawLine(s,x):
    for i in range(0,s):
        print(" ", end=""),
    for i in range(0,x):
        print("X", end="")
    print()
    return 



drawLine(0,5)
drawLine(0,4)
drawLine(0,3)
drawLine(0,2)
drawLine(0,1)















#Function to call the drawLine function to draw an image
def drawPicture():
    drawLine(5,1)
    drawLine(4,3)
    drawLine(3,5)
    drawLine(2,7)
    drawLine(1,9)
    drawLine(4,3)
    drawLine(4,3)
    return

#drawPicture()


#input("Press enter to close program")
