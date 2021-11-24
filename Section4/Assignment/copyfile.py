# I had to import these libraries in order for my IDE to pick up the files correctly.
import os.path
import sys

#Take user inputs
original = input("Name of file to be coppied: ")
copy = input("Name of new file: ")

# I had to use these libraries in order for my IDE to pick up the files and directory correctly.
file = open(os.path.join(sys.path[0], original))
new = open(os.path.join(sys.path[0], copy), 'w' )
new.write(file.read())

# Close Files
file.close()
new.close()