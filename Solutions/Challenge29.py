

print("----HOLIDAY CHECKLIST----")

#Creates the empty arrays
packList=[]
tasks=[]

#Asks the user to input the holiday info
name=input("Enter the destination of the holiday: ")
itemsNum=int(input("Enter the number of items you need to pack: "))
tasksNum=int(input("How many tasks do you need to complete to prepare for the holiday?: "))

#Loop to store the packing list
for i in range(0,itemsNum):
    packList.append(input("Enter the name of item "+str(i+1)+": "))

#Loop to store the tasks
for i in range(0,tasksNum):
    tasks.append(input("Enter task "+str(i+1)+": "))

#Stores the checklist in a file
file = open((name+" checklist.txt"), "w")
file.write("Destination: "+name+"\nPacking List: \n")
for item in packList:
  file.write(item+"\n")
file.write("Tasks: \n")
for item in tasks:
  file.write(item+"\n")
file.close()
print("Your list has been saved")


input("Press enter to close program")
