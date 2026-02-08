#program using parameterized constructor.(Employee Data)

print("***_____Employee Data_____***")
class Employee:                                                     #class name
    def __init__(self,empid,empname,salary,department):
        self.empid=empid
        self.empname=empname
        self.salary=salary
        self.department=department
    def display(self):
        print("Employee ID: ",self.empid)
        print("Employee Name: ",self.empname)
        print("Employee Salary: ",self.salary)
emp1=Employee(101,"akshay",50000,"HR dept")
emp2=Employee(102,"Sanjay",65000,"Finance dept")
emp1.display()
emp2.display()