from math import pi

class FindAreas:
    number = 1
    def Circle(self,rad):
        self.rad = rad
        self.areaCirc = pi * pow(rad,2)
        return self.areaCirc
    
    def Rectangle(self, sideA, sideB):
        self.sideA = sideA
        self.sideB = sideB
        self.areaRect = sideB * sideA
        return self.areaRect

# Instantiate an Object
#myObj = FindAreas()

#print(myObj.number)

#areaCirc = myObj.Circle(6)
#area = FindAreas().Circle(6)
#print(areaCirc)
#print(area)