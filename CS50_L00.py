import math 
import os
"""
# Get a user's first name, 
# Greet the user by their name
# title() capitalize first letter of each word
name = (input("What's your name: ")).strip().title() 
print (f"hello, {name}")
length = len(name)
print(f"length of the name is: {length}")
# another way to achieve the above

# print("hello, ", sep="", end='') # Defualt: sep=" ", end="\n";
# print(name)

# docs.python.org

# Split user's name into first and last name 
first, last = name.split(" ")
print (f"First Name: {first} \nLast Name: {last}")
"""
"""
def main(): 
    name = input("Enter your full name: ").strip().title()    
    greeting(name)
    return name


def greeting(name):
    print(f"Hello, {name}")

main()
"""
"""
def main():
    x = int(input("x: "))
    print(f"x squared is: {square(x):,.2f}")

def square(n):
    return (pow(n, 2))

main()
"""













