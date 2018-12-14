name = input("name please")


markmaths=int(input("Enter the mark for maths: "))



if markmaths>=75:
    markmathsS = "A"
elif markmaths>=60:
    markmathsS = "B"
elif markmaths>=35:
    markmathsS = "C"
else:
    markmathsS = "D"

#print(markmaths)

markE=int(input("Enter the mark English: "))

 
if markE>=75:
    markES = "A"
elif markE>=60:
    markES = "B"
elif markE>=35:
    markES = "C"
else:
    markES = "D"

markS=int(input("Enter the mark Science: "))
  
if markS>=75:
    markSS = "A"
elif markS>=60:
    markSS = "B"
elif markS>=35:
    markSS = "C"
else:
    markSS = "D"



avgrade = int(markmaths+markE+markS)/3

if avgrade>=75:
    avgradeS = "A"
elif avgrade>=60:
    avgradeS = "B"
elif avgrade>=35:
    avgradeS = "C"
else:
    avgradeS = "D"


print(name, "You got a", markmathsS, "in maths, a", markES,"in English and an", markSS, "in science. Your average grade is", avgradeS)


