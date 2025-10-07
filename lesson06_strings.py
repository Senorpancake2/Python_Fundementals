# Basic string creation and indexes:
greeting = "Hello"
name = "Ada"
print(greeting, name)



message = greeting + " " + name + "!"
print("Concatenated message", message)

second_letter = greeting[1]
print(second_letter)

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
print("\nUppercase", phrase.upper())
print("Lowercase",phrase.lower())
print("Capitalize",phrase.capitalize())