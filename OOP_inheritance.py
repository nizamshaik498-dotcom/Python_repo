#Created a program using class and inheritance 

class Animal:
   def sound(self):
      print("Animal Sound")
class Dog(Animal):
   def bark(self):
      print("Barking")

d=Dog()
d.sound()
d.bark()