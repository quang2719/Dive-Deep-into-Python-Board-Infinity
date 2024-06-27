class Person1:
    
    def __init__(self):
        self.name = "Quang"
        self.location = "Ha Noi"
    def introduce(self):
        print(f"My name is {self.name}, I live in {self.location}")

A = Person1()
A.introduce() #My name is Quang, I live in Ha Noi


class Person2:
    #two initial function, the last function will retained
    #previous function will be overiten
    def __init__(self):
        self.name = "Quang"
        self.location = "Ha Noi"
    def __init__(self, name, location):
        self.name = name
        self.location = location
    def introduce(self):
        print(f"My name is {self.name}, I live in {self.location}")

A = Person2() # error missing arg
B = Person2('B',"HCM") #My name is B, I live in HCM
B.introduce()