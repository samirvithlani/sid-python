def demo(name):
    return name.upper()

def test(name):
    return name.lower()



def display(fun):
    fname = fun("samir")
    return fname
    
print(display(demo))
    