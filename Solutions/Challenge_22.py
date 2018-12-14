# Challenge 22

def calculate(xdistance,xtime):
    average = xdistance/xtime
    print("average = ", round(average,2))


distance=int(input("Enter the distance travelled in metres: "))
time=int(input("Enter the time it took to complete the journey in seconds: "))
calculate(distance,time)


def calculate(xdistance,xtime):
    xaverage = xdistance/xtime
   # print("average = ", round(average,2))
    return xaverage


distance=int(input("Enter the distance travelled in metres: "))
time=int(input("Enter the time it took to complete the journey in seconds: "))
average = calculate(distance,time)
print("average = ", average)

