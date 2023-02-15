#AS CCONSTRUCTOR

class Person:
    def __init__(self, name, age):
        print("Person Constructor")

    def print(self):
        print("Person Print")       

class User(Person):
    
    def __init__(self):
        #super().__init__()
        print("User Constructor")
    def print(self):
        super().print()
        print("User Print")
        
    def test(self):        
        super().print()
        
        
u = User()        
u.test()
                