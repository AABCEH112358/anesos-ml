import math 

while True: 
    x = float(input("x: "))
    op = input("operation: ").strip()
    y = float(input("y: "))

    if op == "+":
        r = x + y 
    elif op == "-":
        r = x - y
    elif op == "*":
        r = x * y 
    elif op == "/":
        r = x / y  
    print(r)

    # round(num, [ ,ndigits])
    # int division, 

    