class Employee:
    
    #keyword arguments
    #name , age, salary
    def __init__(self,**kwargs):
        #it's not local varible....
        self.name = kwargs.get("name")
        self.age = kwargs.get("age")
        self.salary = kwargs.get("salary")
    
    def printEmployeeData(self):
        print("Employee Name: ",self.name)
        print("Employee Age: ",self.age)
        print("Employee Salary: ",self.salary)
        


emp = Employee(name="John",age=25,salary=50000)     
emp.printEmployeeData()
        