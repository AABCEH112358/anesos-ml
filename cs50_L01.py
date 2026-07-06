import math 
import os


"""
x = int(input("x: "))
y = int(input("y: "))

if x < y:
    print("y is greater than x")

elif x == y: 
    print("y equal x")

else: print("x is greater than y")
"""
"""
# Probelm: x is odd/even and prime 
x_is_even = False
if x % 2 == 0: 
    x_is_even = True

print(f"{x} is even" if x_is_even else f"{x} is odd", sep = '', end = " ")

x_is_prime = True

if x == 2:
    x_is_prime = True

elif x_is_even:
    x_is_prime = False

else:
    for i in range (2, x):
        if x % i == 0:
            x_is_prime = False
            break

print("and is a prime" if x_is_prime else "but is not a prime" if not x_is_even and not x_is_prime else "and is not a prime")
"""
"""
x = int(input("x: "))
# y = int(input("y: "))

if x < 0 or x > 100: 
    print("Invalid input")
elif x >= 90:
    print("Grade: A")
elif x >= 80:
    print("Grade: B")
elif x >= 70: 
    print("Grade: C")
elif x >= 60: 
    print("Grade: D")
else: 
    print("Grade: F")

# python allows: 10 <= x < 15, for example
"""

model = input("Enter a model name: ").lower()

# match like switch in cpp

match model: 
    case "Sonnet" | "Opus" | "Fable" | "Mythos":
        print("is an anthropic-claude model")
    case "chatgpt":
        print("Is an openai model")
    case _:
        print("Not a good american model yet (as of July 2026)")










































