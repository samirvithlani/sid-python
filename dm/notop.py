choice = int(input("Enter your choice: "))

if choice is not 20:
    print("You are not eligible to vote")
else:
    print("You are eligible to vote")
    
no1 = 10
no2 = 20

# if no1>no2:
#     print("No1 is greater")
#      x = no1

# else:
#     print("No2 is greater")    

#ternery 
x = no1>no2 and no1 or no2 
print("x = ",x)