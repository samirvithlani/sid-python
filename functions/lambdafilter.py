data = [12,25,65,78,30,32,15]

even_list = []
# for i in list:
#     if i %2 ==0:
#         even_list.append(i)

even_list = list(filter(lambda x:(x%2==0),data))

print(even_list)  



employees = [12500,25632,78000,96325,7800,56000]
filterdemp =[]
filterdemp = list(filter(lambda x:(x>50000),employees))
print(filterdemp)








      
