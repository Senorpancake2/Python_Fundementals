# CONDITIONALS IN PYTHON
# comparison operators: ==, !=, <, >, <=, >=
# logical operators: and, or, not
# control flow: if, elif, else

print()
print("--- CONDITIONALS IN PYTHON ---")

print(3 == 2)
print("Hello" == "hello")
print(7 != 4)
print(4 > 5)

#if
print()
num = 10
if num == 10: 
    print("Your number is equal to 10")

num2 = 5
if num2 <= 12:
    print("Your number is less than or equal to 12")
else:
    print("Your number is no less than or equal to 12")

#if elif else
print()

temperature = 72
if temperature > 80: 
    print("It's hot!")
elif temperature >= 60:
    print("It's nice")
else:
    print("It's  cold")

x = 5
y = 5

if x == y:
    print("x is equal to y")
elif x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")

age = 18
has_permission = True

if age >=17 and has_permission:
    print("You can drive")
else:
    print("Can't drive yet")

#USING 'OR' AND 'NOT'
day = "Sunday"
if day == "Saturday" or day is "Sunday":
    print("It's the weekend")
elif day == "Monday":
    print(":|") 
else: 
    print("Not the weekend yet")

