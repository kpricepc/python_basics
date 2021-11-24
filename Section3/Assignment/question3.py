# Define a boolean variable for the while loop
x = True

# Define a list
list = []

while x == True:
    info = input("Please enter a number: ")
    if info != "":          # Check first that input is not null
        info = int(info)    # Convert input into Integer
        list.append(info)   # Append integer to list
    else:
        x = False           # Exit while loop if null is returned

print("The sum of the provided numbers is: " + str(sum(list)))                # Print the Sum of numbers
print("The average of the provided numbers is: " + str(sum(list)/len(list)))  # Print the average of numbers