# Lists store multiple values in one variable.
# They are ordered, mutable (changeable), and allow duplicates.

print()
print("--- Lists in Python ---")

animals = ["Donkey", "Pangolin", "Blobfish"]
numbers = [2, 4, 6, 8, 10]
mixed = ["piffle", 41, True, 9.99]

print(animals)
print(numbers)
print(mixed)

print()
print()
print()
print("--- Indexing: how to access the elements of a list ---")
print("First Element:", animals[0])
print("Second Element:", animals[1])
print("Last Element:", animals[-1])

print()
print("---Modifying Lists---")
animals[0] = "Babirusa"
print(animals)

#ADDS ELEMENT AT THE END OF LIST
animals.append("Glass frog")
print(animals)

#Insert element at specific index
animals.insert(3,"Aye-Aye")
print(animals)
animals.insert(0,"Camel")
print(animals)

animals.remove(animals[4])
print(animals)

last_animal = animals.pop(-1)
print("Last animal:", last_animal)
animals.remove(animals[1])
animals.insert(1,last_animal)
print(animals)

animal_to_replace = animals.index("Pangolin")
print(animal_to_replace)
animals[animal_to_replace] = "Seamonkey"


#initialize a list with brackets:
print()
empty_list = []
empty_list.append("Thing")
print(empty_list)

print()
nums = [3,7,1,9,4,2,5,8,6,0]
print("Original numbers:", nums)

print("Length of list:", len(nums))
print("Min", min(nums))
print("Max:", max(nums))
print("Sum:", sum(nums))
nums.sort()
print("Sorted list:", nums)
animals.sort()
print(animals)

print()

if "cat" in animals:
    print("Cat is in the list")
else:
    print("Cat is not part of the list")

new_list =[1,2,3]
copied_list = new_list.copy()
copied_list.append(4)
print(new_list)
print(copied_list)


#Nested lists/Matrix
print()
matrix = [ [1,2,3], [4,5,6], [7,8,9] ]


print(matrix[0][2])
print(matrix[2][2])

#Challeges

#1:
integer_list = [1,2,3,4,5,6]
number = int(input("Enter a number:"))
replace = integer_list.index(3)
integer_list[replace] = number

print(integer_list)

shopping = []
shopping.append("Chicken, Egg, Ham")
shopping.insert(1,"Beef")
shopping.remove("Ham")
print(shopping)