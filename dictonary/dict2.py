data ={"user1":{1:"raj",2:"ram"},"user2":{1:"parth",2:"priya"}}
print(data['user1'][2])

for k,v in data.items():
    print(k)
    for k1,v1 in v.items():
        print(k1,"==",v1)