class Person:
    def __init__(self, name, location):
        self.name = name
        self.location = location
    def introduce(self):
        print(f"My name is {self.name}, I live in {self.location}")

class Student(Person):
    def __init__(self,name, location, code, class_code,age):
        Person.__init__(self,name,location)
        self.code = code
        self.class_code = class_code
        self.age = age
    def introduce2(self):
        print(
            f"""My name is {self.name}, I live in {self.location}
            my code is {self.code}, my class code is {self.class_code}
            and I'm {self.age} years old!""")

A = Student('Quang','HN','S1','CL1',10)
A.introduce2()