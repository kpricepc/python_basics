class Dog:
    tricks = []
    def __init__(self, name):
        self.name = name
    def add_trick(self, trick):
        self.tricks.append(trick)

e = Dog("Graham")
e.add_trick("Sit")
e.add_trick("Stay")
print(e.tricks)