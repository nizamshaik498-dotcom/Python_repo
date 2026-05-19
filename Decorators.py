#Created a program using decorators 

def coding(code):
    def program():
        print("program started")
        code()
        print("Program is under running state")
    return program
@coding
def login():
    print("Login Successfully")
login()