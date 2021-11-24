# I had to import these libraries in order for my IDE to pick up the files correctly.
import os.path
import sys

# Create a list
myList = []

# Ask for file to use
file1 = input("Name of file: ")

# I found the "with" keyword handy for opening files
with open(os.path.join(sys.path[0], file1)) as file:
    # Separate into lines
    lines = file.readlines()
    for x in lines:
        # Separate into words
        words = x.split()
        for y in words:
            # Remove special characters , and .
            y = y.replace('.', ' ')
            y = y.replace(',', ' ')
            # Remove Spaces
            y = y.strip()
            # Make everything lower case
            y = y.lower()
            if y not in myList:
                # Add to list if non existant
                myList.append(y)

# Sort the list
myList = sorted(myList)

# Iterate through the list and print each entry
print("Words in file, in aplphabetical order...")
for x in range(len(myList)):
    print(myList[x])