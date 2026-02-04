#python program created using single inheritance.
class Animal:                           #class Animal
    def speak(self):                   
        print("Animal Sound")
class Dog(Animal):                      #class Dog inherited from class Animal           
    def bark(self):
        print("Barking sound")
d=Dog()
d.speak()
d.bark()