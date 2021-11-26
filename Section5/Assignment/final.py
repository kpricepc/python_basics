from ChatSession import ChatSession

# Create object, Import the file
sessionObj = ChatSession('iphone_07_18-1.annot')

# Print Number of lines
TotalLines = sessionObj.GetNumLines()
print("Number of Lines: ", TotalLines)

# Print Tags
Tags = sessionObj.GetTagsList()
print("Tags List: ", Tags)

# Print Time Stamp List
TimeStamp = sessionObj.GetTimesList()
print("Time Stamp List: ", TimeStamp)

# Print Members List
MembersList = sessionObj.GetMembersList()
print("Members List: ", MembersList)

# Print Members Symbols
SymbolList = sessionObj.GetUserSysList()
print("Member Symbol List: ", SymbolList)

# Print Message List
MessageList = sessionObj.GetMessageList()
print("Message List: ", MessageList)

# Print Unique Members List
UniqueMembers = sessionObj.GetUniqueMemberList()
print("Unique Members List: ", UniqueMembers)

# Print Unique Symbols List
UniqueTags = sessionObj.GetUniqueTagList()
print("Unique tags: ", UniqueTags)