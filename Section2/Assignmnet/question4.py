# Is the triangle an equilateral triangle.
print("Please input the 3 sides of your triangle")
x = input("Side #1: ")
y = input("Side #2: ")
z = input("Side #3: ")

if x == y and y == z and z == x:
    print("Your triangle is an equilateral triangle")
else:
    print("Your triangle is NOT and equilateral triangle")
