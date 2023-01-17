list = [1,2,3,24,45,9,78,36,96,23,741,258,99,52,64,72]
sqlist =[]

# for i in list:
#     #sqlist.append(i**2)
#     if i %2 ==0:
#         sqlist.append(i)

    
sqlist = [i for i in list if i %2 ==0 and i > 50]

print(sqlist)