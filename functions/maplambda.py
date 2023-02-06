# purchasePrice = [14,25,36,98,78,36,452,120]
# salesprice =[]
# price =0
# # for i in purchasePrice:
# #     price = i +(i*0.1)
# #     salesprice.append(price)


# salesprice = list(map(lambda x:(x+(x*0.1)),purchasePrice))
# print(salesprice)    


data = ["rajvi","Reena","parth","samir","siddharth","Rahul","ram","rekha"]
fdata =[]
#fdata = list(map(lambda x:(x[0]=="r" or x[0]=="R"),data)  or filter(lambda x:(x[0]=="r" or x[0]=="R"),data))
fdata = list(filter(lambda x:(x[0]=="r" or x[0]=="R"),data) or map(lambda x:(x[0]=="r" or x[0]=="R"),data))
#fdata = list(filter(lambda x:(x[0]=="r" or x[0]=="R"),data))


print(fdata)




    
    
    

