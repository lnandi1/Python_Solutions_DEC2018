def calculate(d,t):
    speed=d/t
   # print("The average speed is:",round(speed,2),"m/s")
    return speed


def main():
    distance=int(input("Enter the distance travelled in metres: "))
    time=int(input("Enter the time it took to complete the journey in seconds: "))
    average = calculate(distance,time)
    print("The average speed is:",round(average,2),"m/s")

main()
