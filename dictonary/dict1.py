#users ={}#blank dictionary
users = {1:"John",2:"Jennie",3:"Jim",4:"Jack",5:"Joe",6:"Jennie",1:"amit"}
#print(users)

users[77]="George"
users[3]="Sia"

#print(users[1])
#print(users.get(11))
#user1 = users.copy()

#print("keys",users.keys())
#print("items",users.items())
#remvedelm = users.pop(33)
#print("values",users.values())
#remvedelm =users.popitem()
#print("removing....",remvedelm)

users.update({12:"neha",4:"jill"})



for k,v in users.items():
    print(k,"==",v)

