#Program created using class polymorphism

class BMW:                                                      #base class
    def car(self):                                              #method of base class
        print("Byrische Motoren Worke")
    def model(self):
        print("M5")
class Lamborghini:
    def car(self):
        print("The bull of cars")
    def model(self):
        print("Aventador")
ob=BMW()
ob1=Lamborghini()
for vehicles in(ob,ob1):
    vehicles.car()
    vehicles.model()
