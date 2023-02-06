
# Decorators are used to add functionality to an existing function without modifying it.
def greetDecorators(func):
    print("Inside greetDecorators")
    def inner(msg):
        print("Inside inner")
        res = func(msg)
        print(res)
        return res
    
    print("Returning inner")
    return inner


@greetDecorators
def greeting(msg):
    print(msg)
    #return msg.upper()

greeting("Hello")
#print(greeting("Hello"))

