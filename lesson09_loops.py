#Loops repeat a block of code until they hit a limit or condition
#Exist to help save time in typing the same lines multiple times
print()

#for-loop
#for-loop repeats for each element in a sequence like a list or string

import time

animals = ["Lamb","Sheep","Cow","Goose","Donkey"]

print("\nOur animals:", animals)

for animal in animals:
    print("Now petting a",animal)
    time.sleep(1.5)
    if animal == "Sheep": print("Hi Shep")
print("\nNo animals left to pet")

print()
print("---range(Start, Stop, Step)---")
for num in range(2, 11, 2):
    print("Even number counting:",num)


print()
print("---Iterating over strings---")

fav_word = "Shenanigans"
letter_list = []

for letter in fav_word:
    print(letter,end="")
    letter_list.append(letter)
    print(letter_list)
    
print()

#WHILE LOOPS

#while loop repeats while the condition is true

count = 0
while count < 5:
    print(f"Loopin'. We are on loop # {count}.")
    count+=1
    time.sleep(0.5)
print("We have escaped the loop")

user_input = ""

while user_input != "exit":
    user_input = input("Type 'exit' to escape:")


count = 60
increment = 1

while count > 0:
    count-= increment
    increment += 1
    print(count)

    if count < 0:
        break

#  :O 67
import random
number_of_fruits = int(input("Enter number of fruits: "))

fruits = ["Banana","Apple","Mango","Strawberry","Blueberry"]

for i in range(number_of_fruits):
    print("you picked a ", random.choice(fruits))