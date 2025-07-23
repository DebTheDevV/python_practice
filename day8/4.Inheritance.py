class Animal :
    location = "australia"
    def __init__(self  , name):
        self.name = name 
    def speak(self):
        print("Speaking now ...")

class Dog(Animal): # dog is the child class of Animal
    def speak(self):
        super().speak() #we r using the speak function of the parent class
        print("woof")

a = Animal("dog")
a.speak()


d=Dog( "Rocky")
d.speak()
print(d.location)

#super - Inside a. child class. super() lets you call methods from the parent class , This is useful when you want to extend the parent's behaviour instead of completely replacing it.. IT is especially important  when initializinf the parent's class part of a child object
