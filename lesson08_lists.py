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