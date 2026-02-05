#program created using multilevel inheritance

class Animal:                                   #base class
    def speak(self):                            #method of base class
        print("Animal Sound")
class Dog(Animal):                              #derived class inheriting from base class
    def bark(self):                             #method of derived class
        print("Barking sound")
class puppy(Dog):                                  #derived class inheriting from derived class
    def weep(self):                                #method of derived class
        print("Weeping sound")
d=Dog()
d.speak()
d.bark()