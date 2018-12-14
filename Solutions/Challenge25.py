

print("----CLUB SIGN UP----")


first=input("Enter your first name: ")
last=input("Enter your last name: ")
gender=input("Enter your gender: ")
form=input("Enter your form: ")

#Opens the file or creates it if it doesn't already exist
file = open("signup.txt", "a")
#Records the user's details in the file
file.write("\nFirst name: "+first+", Last name: "+last+", Gender: "+gender+", Form: "+form)
#Closes the file
file.close()


input("Press enter to close program")
