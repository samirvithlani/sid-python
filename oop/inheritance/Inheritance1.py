#single...

class Demo(object):
    
    def __init__(self):
        print("Demo Constructor")

d = Demo()

#single level inheritance
class Vehicle:
    #instance variable
    vehName =""
    price = 0
    
class Car(Vehicle):
    
    def getVehData(self):
        self.vehName = "BMW"
        self.price = 1000000
        
    def printVehData(self):
        print("Vehicle Name: ",self.vehName)
        print("Vehicle Price: ",self.price)   
#multiple inheritance        
class Bike(Vehicle):
    def getVehData(self):
        self.vehName = "KTM"
        self.price = 250000
        
    def printVehData(self):
        print("Vehicle Name: ",self.vehName)
        print("Vehicle Price: ",self.price)   
    
            
        
c = Car()
c.getVehData()
c.printVehData()  
b= Bike()
b.getVehData()
b.printVehData()