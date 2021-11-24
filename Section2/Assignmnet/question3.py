# Arithmetic operator on varibales
x = 5
y = 10

operator = input("Please input an arithmetic operator, +, -, *, or / ")

if operator == '+':
    print(x+y)
elif operator == '-':
    print(x-y)
elif operator == '*':
    print(x*y)
elif operator == '/':
    print(x/y)
else: 
    print("Could not determine operator.")