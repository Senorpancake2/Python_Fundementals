# #CHALLENGE_1: PALIDROME
# word = input("Enter a word: ")
# if word == word[::-1]: print("Your word is a palidrome")
# else: print("Your word is not a palidrome")


# #Challenge_2: Email
# email = input("Enter your email: ")
# index = email.index("@")
# print(index)
# print(email[index+1:])



# #Challenge_3: First and last match

# list = ["Apple","Bannana","Orange"]
# print(list)
# response= input("Enter the last element in the list: ")
# if response == list[2]:print(True)
# else: print(False)


#Challenge_4: Suffix adder

word2 =input("Enter a word: ")
if len(word2) <= 3:
     print(word2)
elif word2[-3:] == "ing": print(word2+"ly")
else: print(word2+"ing")