input_file = open('test.txt')
for line in input_file:
    if line.find("From:"):
     print(line)