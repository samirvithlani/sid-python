class User:
    
    name ="x"
    
    def __init__(self):
        print("User Object Constructed")
        self.name = "NA"
    
    def getUsers(self,name):
        pass
        #self.name = input("Enter Name: ")    
        #self.name = name
        
    def printUser(self):
        print("User Name: ",self.name)    



u1 = User() #seperate object / copy
u2 = User() #seperate object / copy


u1.getUsers("John")
u1.printUser()

u2.getUsers("Fionna")
u2.printUser()

        