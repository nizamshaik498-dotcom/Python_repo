#program created using hybrid inheritance.

class ceo:                                          #base class
    def ceomethod(self):                            #method of ceo class
        print(("I am the ceo"))
class manager(ceo):                                 #derived class of ceo class
    def managermethod(self):                        #method of manager class
        print("I am manager")
class employee1(manager,ceo):
    def employee1method(self):
        print("I am employee 1")
emp1=employee1()
emp1.ceomethod()
emp1.managermethod()
emp1.employee1method()