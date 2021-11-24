#Tuples are static, and lists you can modify
myList = [0,1,2,3,4,5,6,7,8,9]
mySentence = "This is a sentence."
myList.append(10)

print(myList)

myList.extend([11,11,12,13])

print(myList)

# Removes a specific index number
print(myList.pop())

print(myList.count(11))

print(mySentence.count(" "))

