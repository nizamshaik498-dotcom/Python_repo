#program made using class and object (oops)

class student:
    def get(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("My name is :",self.name)
        print("My age is: ",self.age)
stud1=student()
stud1.get("Mike",20)
stud1.display()