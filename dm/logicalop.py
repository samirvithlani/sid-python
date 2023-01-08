hours = int(input("Enter the hours: "))
exp = int(input("Enter the experience: "))

'''
    hours>4000 and exp >5
    T     T    T
    T      F   F
    F     -  F


    T  -  T
    F  T  T
    F  F  F


'''
if hours>4000 or exp >5:
    print("You are eligible for promotion")
    
elif exp>7:
    print("You are eligible for promotion") 

else:
    print("You are not eligible for promotion")    