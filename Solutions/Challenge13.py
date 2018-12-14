#!/usr/bin/python3

#asks the user to input a sentence and stores it in the text variable
text=input("Enter your sentence: ")
word1=input("Enter the word you want to replace: ")
word2=input("Enter the word you want to replace it with: ")

#outputs the sentence with the original word replaced with the new word
print (text.replace(word1,word2))


input("Press enter to close program")