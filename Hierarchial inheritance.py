#program created using hierarchial inheritance.

class manager:
    def managermethod(self):
        print("I am manager")
class employee1(manager):
    def employee1method(self):
        print("I am employee1")
class employee2(manager):
    def employee2method(self):
        print("I am emloyee2")
e1=employee1()
e2=employee2()
e1.managermethod()
e1.employee1method()
e2.managermethod()
e2.employee2method()
