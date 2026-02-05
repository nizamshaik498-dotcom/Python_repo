#program created using multiple inheritance.

class calculation1:
    def summation(self,a,b):
        return a+b
class calculation2:
    def subtraction(self,a,b):
        return a-b
class calculation3:
    def multiplication(self,a,b):
        return a*b
class derived(calculation1,calculation2,calculation3):
    def division(self,a,b):
        return a/b
    
c=derived()
print("The summation value: ",c.summation(10,20))
print("The subtraction value: ",c.subtraction(10,20))
print("The multiplication value: ",c.multiplication(10,20))
print("The division value: ",c.division(10,20))