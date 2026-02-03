#program amade using constructor (default constructor)
class student:                                  #class name
    def __init__(self):                         #constructor                                
        self.name="christopher"
        self.age=20
    def call(self):
        print(self.name,self.age)
s1=student()
s1.call()

