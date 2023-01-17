data = {1:"raj",4:"ram",3:"ravi",2:"rohit",5:"krishna"}

valueList = list(data.values())
valueList.sort()
keylist = list(data.keys())

print(valueList)
print(keylist)

#zip
x=  {i:j for i,j in zip(keylist,valueList)}

print(x)




