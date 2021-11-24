myList = (1/3, 1/5, 1/7, 1/9, 1/11, 1/13)

iterations = int(input("How many iterations would you like? "))

if iterations == 1:
    print((1 - myList[0]) * 4)
elif iterations == 2:
    print((1 - myList[0] + myList[1]) * 4)
elif iterations == 3:
    print((1 - myList[0] + myList[1] - myList[2]) * 4)
elif iterations == 4:
    print((1 - myList[0] + myList[1] - myList[2] + myList[3]) * 4)
elif iterations == 5:
    print((1 - myList[0] + myList[1] - myList[2] + myList[3] - myList[4]) * 4)
elif iterations == 6:
    print((1 - myList[0] + myList[1] - myList[2] + myList[3] - myList[4] + myList[5]) * 4)