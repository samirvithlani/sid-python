
num1 = 54
num2 = 24
max =0

if num1>num2:
    max = num1
else:
    max = num2
    

while(True):
    #max = 54
    #54 % 54 == 0 and 24 % 54 == 0
    #55 % 54 == 0 and 24 % 55 == 0
    #216 % 54 == 0 and 24 % 216 == 0
    if max % num1 == 0 and max % num2 == 0:
        print(max)
        break
    max+=1
    #55
    #56
       