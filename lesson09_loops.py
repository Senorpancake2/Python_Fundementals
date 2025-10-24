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
    time.sleep(1)
    if animal == "Sheep": print("Hi Shep")
print("\nNo animals left to pet")

print()
print("---range(Start, Stop, Step)---")
for num in range(2, 11, 2):
    print("Even number counting:",num)
    time.sleep(0.15)

