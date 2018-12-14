def calculate(d,t):
    speed=d/t
    print("The average speed is:",round(speed,2),"m/s")
    #return


def main():
    distance=int(input("Enter the distance travelled in metres: "))
    time=int(input("Enter the time it took to complete the journey in seconds: "))
    calculate(distance,time)
    
main()












