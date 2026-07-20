#input method to take values from user
input("What's your name? ")
#prints on console
print("hello, world")

name = input("What's your name? ")
#Remove whitespace from input str
name = name.strip()
#Capitalize user's name
name = name.capitalize()

#Remove whitespace from input str and Capitalize user's name
name = name.strip().title()

first, last = name.split(" ")
# print("hello, ", name) #adds 2 space after hello,
# print("hello,", name)
# print("hello, ")
# print(name)
print("hello, ", end="???")
print(name)
print("hello, ", name, sep="???")
#single quotes inside double quotes
print("hello, 'Rutuja'")
#double quotes inside single quotes
print('hello, "Rutuja"')
#double quotes inside single quotes using escape sequence
print("hello, \"Rutuja\"")
#most elegant way to use a variable inside print
print(f"hello, {name}")
print(f"hello, {first}")
print(f"hello, {last}")
"""
several line comments
"""
def hello(to="world"):
    print("hello", to)

name = input("What's your name? ")
hello()
hello(name)