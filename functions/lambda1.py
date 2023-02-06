#lambda : in a python kambda function ia a special type of function which is used to create a function
# without a name

msg = lambda:print("hello world")
msg()


# def name(x):
#     print("hello",x)
# name()

name = lambda x,y: print("hello",x,y)

name("python","world")


ans = lambda a,b : a+b
print(ans(10,20))


flag = lambda a,b: print("a is bigger") if a>b else print("b is bigger")
flag(1,2)


# def flag1(a,b):
#     if a>b:
#         return a
#     else:
#         return b

flag1 = lambda a,b : a if a>b else b
x = flag1(100,200)
print(x)



