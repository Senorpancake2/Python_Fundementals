# python functions are simply blocks of code that can be reused
# To run a function, you "call" the function by writing it's name, followed by parenthesis, and any arguements


print("\nFunctions(Procedures)")

print("\nExample 1:\n")

def say_hi():
    print("Hi")

def say_bye():
    print("Bye")

say_hi()
say_bye()

print("\nExample 2:\n")

def express_this(e): # e is called a PARAMETER, which is a placeholder for an ARGUEMENT
    return e

expression1 = express_this(1 + 2)
print(expression1)
expression2 = express_this(45 * 6)
print(expression2)


def greeter(n):     #n is the parameter
    return f"Hi {n}"

first = greeter("Yuji")
second = greeter("Todo")
third = greeter("Choso")

print(first,second,third)

def remainder(a,b):
    return a % b

result = remainder (3,2)
print("Remainder:", result)

def is_far(distance):
    #INSERT BASE CASE
    if distance < 1:
        return "Error"


    if distance >= 100:
        return "That's far"
    elif distance < 100 and distance > 20:
        return "That's not too far"
    elif distance <= 20:
        return "That's close"
    
print(is_far(250))
print(is_far(75))
print(is_far(20))
print(is_far(-4))


def double_sequencer(number,times):
    value = number
    sequence = []
    for i in range(times):
        value = value * 2
        sequence.append(value)

    return sequence

result = double_sequencer(1,10)

print(result)