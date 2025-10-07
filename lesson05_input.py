#USER INPUT IN PYTHON

print("\n--- User Input Demonstration ---")

name = input("Enter your name: ")
print("Hello",name)

age = int(input("Enter your age: "))
print(type(age))

# Example with float input
height = float(input("Enter your height in meters: "))
print("You are", height, "meters tall.")

#CHALLENGE 1
Color = (input("Enter your favorite color:"))
print("Your favorite color is", Color)

#CHALLENGE 2
number1 = (int(input("Enter your favorite number:")))
number2 = (int(input("Enter another number:")))
print("Total:",number1+number2)

#CHALLENGE 3
import math

diameter = (int(input("Enter a diameter for a circle:")))
radius = diameter/2
print("Area:",radius**2*math.pi )

#CHALLENGE 4
import random

die_sides = (int(input("Enter Number of sides for die:")))
die_roll = (random.randint(1,die_sides))
print(die_roll)