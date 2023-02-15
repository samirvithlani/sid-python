class Sum:    
    no1 = 10
    no2 = 20

class Sub:
    no1 = 100
    no2 = 50


class Calc(Sum,Sub):
    
    def sumData(self):
        return self.no1 + self.no2
    
    def subData(self):
        return self.no1 - self.no2


c = Calc()
print(c.sumData())
print(c.subData())

    


        