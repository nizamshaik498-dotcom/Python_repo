#python program created using python overriding method.

class vehicle:                                                              #base class
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def show(self):
        print("details: ",self.brand,self.model,self.price)
    def maxspeed(self):
        print("The max speed is over 250")
    def gearsystem(self):
        print("Manual gear system")
class car(vehicle):
        def maxspeed(self):
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
