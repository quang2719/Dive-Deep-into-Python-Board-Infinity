class Animal:
    def speak(self):
        print("Generic animal sound")

class Dog(Animal):
    def speak(self):
        print("Gooo Gooo!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

animals = [Dog(), Cat(),Animal()]
for animal in animals:
    animal.speak()  
    #Gooo Gooo!
    #Meow!
    #Generic animal sound
