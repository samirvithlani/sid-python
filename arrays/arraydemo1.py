#array,list,set,dictionary,tuple
import array as arr
#c,c,B,u,h,H,i,I,l,L,f,d

a =arr.array('i',[1,2,3,4,5,6,7,8,9,10,15,25])

length = len(a)

# for i in range(0,len(a)):
#     print(a[i])


    
a.append(100)   
a.insert(4,200) 
a.extend([12,25,46,78,90,100])
for i in a:
    print(i," ",end="")
#a.remove(100)
#removedElm = a.pop()
#removedElm = a.pop(4)
#a.reverse()
x = a.index(200,0,5)

print("x = ",x)
#print("removing element",removedElm)

print("\n")
for i in a:
    print(i," ",end="")