#program created using multilevel inheritance

class Animal:                                   #base class
    def speak(self):                            #method of base class
        print("Animal Sound")
class Dog(Animal):                              #derived class inheriting from base class
    def bark(self):                     
        print("Barking sound")
d=Dog()
d.speak()
d.bark()