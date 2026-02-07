#Program created using class polymorphism

class BMW:                                                      #base class
    def car(self):                                              #method of base class
        print("Byrische Motoren Worke")
    def model(self):                                            #method of base class
        print("M5")
class Lamborghini:                                              #derived class                                 
    def car(self):                                              #method of derived class
        print("The bull of cars")
    def model(self):                                            #method of derived class                                            
        print("Aventador")
ob=BMW()
ob1=Lamborghini()
for vehicles in(ob,ob1):                                        #polymorphism
    vehicles.car()
    vehicles.model()
