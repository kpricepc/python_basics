
myList = [2,3,4,5,8,4,6,3,4,6,8,9,7,5,3,5,7,4,3,2,2,1,4,6,8,6,8,9,3]
yourList = [10,20,30,40]
emptyList = []

# Function for mode
def mode(modeList):
    empty(modeList)
    print("Mode of list is: " + str(max(set(modeList), key = modeList.count)))

# Function to check middle list value
def median(medianList):
    empty(medianList)
    # Sort the List
    medianList = sorted(medianList)
    # Find the median
    mid = (len(medianList) -1) / 2
    # Print the median value
    print("Median of list is: " + str(medianList[int(mid)]))

# FUnction to calculate mean
def mean(meanList):
    empty(meanList)
    print("Mean of list is: " + str(sum(meanList) / len(meanList)))

# Function to check if list is empty
def empty(emptyList):
    if emptyList == []:
        print("0")
        
# So you can change the list input easily
List = myList

# Go through all the functions
if __name__ == '__main__':
    try:
        mode(List)
        median(List)
        mean(List)
    except:
        print("Exit")
