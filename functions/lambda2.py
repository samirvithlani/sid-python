listdata = [lambda arg=x: arg *10 for x in range(1,6)]

for i in listdata:
    print(i())
    
#sort    
data =[[14,1,65],[5,9,3,78]]    
sortlist  = lambda x:(sorted(i) for i in x)
for i in sortlist(data):
    print(i)

#convert list to nested list
data1 = [1,2,3,67,4]    
temp =[]

for e in data1:
    temp.append([e])

sorttemp = lambda x:(sorted(i) for i in x)
for i in sorttemp(temp):
    print(i)    

#print(temp)    