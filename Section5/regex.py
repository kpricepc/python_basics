import re

email1 = "joe@gmail.com"
email2 = "kyle@gmail.com"
filter1 = re.search("[@]gmail.com", email1)
filter2 = re.search("[@]yahoo.com", email2)
print(filter1)
print(filter2)
#UniqueList = list(filter(filter.match, ))
#print(UniqueList)

#txt = "I am at my in-laws for Thanksgiving. We are at the farm, and there is so much food to be eaten."

#x = re.findall("m", txt)

#print(x)