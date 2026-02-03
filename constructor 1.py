#program amade using constructor (default constructor)
class student:
    def __init__(self):
        self.name="christopher"
        self.age=20
    def call(self):
        print(self.name,self.age)
s1=student()
s1.call()

