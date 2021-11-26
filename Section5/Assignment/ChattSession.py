# I had to import these libraries in order for my IDE to pick up the files correctly.
import os.path
import sys

class ChatSession:
    def __init__(self,filename):
        # All the Variables to be used
        self.numLines = 0
        self.TagsList=[]
        self.MembersList=[]
        self.TimesList=[]
        self.UniqueMembersList=[]
        self.UniqueTagsList=[]
        self.MessageList=[]
        self.UserSysList=[]
        
        # Open the file
        f = open(os.path.join(sys.path[0], filename), "r")
        
        # Read each line in file
        records = f.readlines()

        # Iterate over each line in file
        for record in records:
            # Count each line
            if record:
                self.numLines += 1

            # Make file into a strings, 
            # everything after the 4th split is the message.
            Strings = record.split(' ', 4)

            # Grab the Tag
            self.TagsList.append(Strings[0])

            # Grab the Time Stamp
            self.TimesList.append(Strings[1])

            # Grab the Member
            self.MembersList.append(Strings[2])

            # Grab the Members Symbol
            self.UserSysList.append(Strings[3])

            # Grab the message entry
            self.MessageList.append(Strings[4].strip().split('\n'))

            #Find Unique Members
            if Strings[2] not in self.UniqueMembersList:
                self.UniqueMembersList.append(Strings[2])

            # Find Unique Tags    
            if Strings[0] not in self.UniqueTagsList:
                self.UniqueTagsList.append(Strings[0])            

    # Number of Lines function
    def GetNumLines(self):
        return self.numLines
    
    # All tags list
    def GetTagsList(self):
        return self.TagsList

    # The Timestamp list
    def GetTimesList(self):
        return self.TimesList

    # The Members list
    def GetMembersList(self):
        return self.MembersList

    # The unique members list
    def GetUniqueMemberList(self):
        return self.UniqueMembersList

    # THe Unique tag list
    def GetUniqueTagList(self):
        return self.UniqueTagsList

    # The message list
    def GetMessageList(self):
        return self.MessageList

    # The User symbol list
    def GetUserSysList(self):
        return self.UserSysList