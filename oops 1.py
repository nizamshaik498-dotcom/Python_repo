#program created using class and object (oops) using a constructor (__init__ method)

class student:                                  #class name
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("My name is: ",self.name)
        print("My age is: ",self.age)
stud=student("Max",20)
stud.display()