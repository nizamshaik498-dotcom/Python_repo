#python program created using python overriding method.

class vehicle:                                                              #base class
    def __init__(self,brand,model,price):                                   #constructor
        self.brand=brand
        self.model=model
        self.price=price
    def show(self):                                                         #method to show the details of the vehicle
        print("details: ",self.brand,self.model,self.price)
    def maxspeed(self):                                                     #method to show the max speed of the vehicle
        print("The max speed is over 250")
    def gearsystem(self):                                                   #method to show the gear system of the vehicle
        print("Manual gear system")
class car(vehicle):                                                         #derived class                                                 
        def maxspeed(self):                                                 #overriding the maxspeed method of the base class
            print("The maxspeed is over 410")
        def gearsystem(self):
            print("Automatic gearsystem")
c1=car("BMW","M5",90000000)
c1.show()
c1.maxspeed()
c1.gearsystem()

c2=vehicle("Audi","R8",50000000)
c2.show()
c2.maxspeed()
c2.gearsystem()
