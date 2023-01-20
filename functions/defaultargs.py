def avg(x=0,y=0,z=0):
    return (x+y+z)//3


print(avg(20,20))
    
#keyword argument    
def employee(firstname,lastname):
    print("firstname",firstname)
    print("lastname",lastname)
        
employee(firstname="raj",lastname="kumar")

#args *argv
def test(*argv):
    print(argv)
    
test("amit","raj","neha")    

#kwargs

def demo2(**kwargs):
    print(kwargs)
    
demo2(firstName="raj",lastName="kumar",age=20)    