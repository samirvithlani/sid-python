data = {1:"raj",4:"ram",3:"ravi",2:"rohit",5:"krishna"}

keys = list(data.keys())
keys.sort()

# for i in keys:
#     print(i,data[i])

sorteddict = {i:data[i] for i in keys}
  
print(sorteddict)