#class name must starts with capital letter
class Bank:
    IFSCCODE = "SBIN0001234"
    #instance variable / class level variable
    #name = ""
    #it will create variable named name and assign value of name given in __init param
    #self will represent current object
    def __init__(self, name):
        name ="raj"
        print("init called")
        print("init--->",name)
        #local variable...
        self.name = name
        

#create an object of class..
bank = Bank("SBI")

print(bank.IFSCCODE)   
print(bank.name)     