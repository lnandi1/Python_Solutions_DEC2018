import random


comp=random.randint(1,3)


user=int(input("Enter your choice:\n1=Rock\n2=Paper\n3=Scissors\n"))


print("The computer has chosen",comp)


if comp==user:
    print ("Tie game")
elif comp==1 and user==3:
    print ("Computer wins")
elif comp==2 and user==1:
    print ("Computer wins")
elif comp==3 and user==2:
    print ("Computer wins")
else:
    print ("You Win!")

