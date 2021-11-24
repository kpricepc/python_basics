# I had to import these libraries in order for my IDE to pick up the files correctly.
import os.path
import sys

#Take user inputs
file1 = input("Name of first file to be compared: ")
file2 = input("Name of second file to be compared: ")

# I had to use these libraries in order for my IDE to pick up the files and directory correctly.
first_file = open(os.path.join(sys.path[0], file1))
second_file = open(os.path.join(sys.path[0], file2))

# Make each line a list entry
first = first_file.readlines()
second = second_file.readlines()

# Compare the two lists, if they are the same, exit the program.
if first == second:
    print("Yes")
    exit

# Loop over list starting with 0, over the minimum of the length of the two strings
for x in range(0,min(len(first),len(second))):
    # Compare the string entries
    if (first[x] != second[x]):
        print("No")
        print("Mismatched Lines: ", first[x])
        print("Mismatched Lines: ", second[x])
        break