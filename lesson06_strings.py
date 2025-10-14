# Basic string creation and indexes:
greeting = "Hello"
name = "Ada"
print(greeting, name)


#CONCATENATION
message = greeting + " " + name + "!"
print("Concatenated message", message)

second_letter = greeting[1]
print(second_letter)

#SPLICING
word = "Supercalifragilisticexpialidocious"
print("First letter:", word[0])
print("Last letter:", word[-1])
print("Range of letters 9-13:", word[9:13])
print("Last seven letters:", word[-7:])
print("Skipping every other letter:", word[::2])
print("Reversed, skipping every third letter:", word[::-3])

print()

#BUILT IN FUNCTIONS

country = "Finland"
length_of_word = len(country)

print(length_of_word)

word_length = len(word)

print(word_length)

phrase = "spongEBOB"
print("\nUppercase:", phrase.upper())
print("Lowercase:",phrase.lower())
print("Capitalize:",phrase.capitalize())
print("Title Format:", phrase.title())#Makes every word capitalized

print("\n---The Replace Function---\n")
sentence = "I'm a goofy goober"
new_sentence = sentence.replace("I'm","You're")
print(sentence)
print(new_sentence)

print("\n----Formatted Strings----\n")

name = "Ada"
age = 28
city = "London"
print(f"Hello, my name is {name}. I am {age} years old. and live in {city}")

# f-strings can do math and function calls inside {}

print(f"Next year, I'll be {age + 1}. My name in uppercase is {name.upper()}.")
#CHALLEGES

print()
quote = input("Enter your favorite quote: ")
print(len(quote))

#Challege 2

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(last_name + "," + first_name)

#CHALLEGE 3

word_1 = input("Enter a word: ")
print(word_1.upper())
print(word_1.lower())
print(word_1[::-1])