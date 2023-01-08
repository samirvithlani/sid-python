age = int(input("Enter your age: "))

if age>=18:
    print("You are eligible to vote")
    if age>=21:
        print("You are eligible to marrige")
    else:
        print("You are not eligible to marrige")    

else:
    print("You are not eligible to vote")        
    if age>=12:
        print("You are eligible to school")
    elif age>=5:
        print("You are eligible to play")             
    else:
        print("You are not eligible to study")    
        
        
    

