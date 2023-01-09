#1634 8208 371
no = int(input("Enter a number: "))
temp = no
temp1 = no
rem = 0
ans =0
count = 0

# length = len(str(no))
# print(length)

while no !=0:
    no = no // 10
    #print(no)
    count+=1
print(count)    
    

while temp1!=0:
    rem = temp1 %10
    ans = ans + rem ** count
    temp1 = temp1 // 10
    
print(ans)    
    