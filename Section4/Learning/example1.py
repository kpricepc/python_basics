import os.path
import sys

fhand = open(os.path.join(sys.path[0],'HumptyDumpty.txt'))
for line in fhand:
    line = line.rstrip()
    words = line.split()
    print(line)
fhand.close()