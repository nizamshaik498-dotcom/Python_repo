#program created using hierarchial inheritance.

class manager:                                  #base class
    def managermethod(self):                    #method of base class
        print("I am manager")
class employee1(manager):                       #derived class1               
    def employee1method(self):                  #method of derived class1
        print("I am employee1")
class employee2(manager):                       #derived class2
    def employee2method(self):                  #method of derived class2
        print("I am emloyee2")
e1=employee1()
e2=employee2()
e1.managermethod()
e1.employee1method()
e2.managermethod()
e2.employee2method()
