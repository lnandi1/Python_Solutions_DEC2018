import random


names=[]

for i in range(1,6):
    names.append(input("Enter name "+str(i)+": "))

print(names)

num=random.randint(0,5)

print(names[num],"has been chosen")


