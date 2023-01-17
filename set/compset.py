users = {"parth","neha","priya","shreya","meet","pr","sr"}
fusers = set()

for i in users:
    if len(i) > 4 or (i.startswith('p') or i.startswith('s')):
        fusers.add(i)
        

#{print(i) for i in users}
#fusers = {i for i in users if len(i) > 4}



print(fusers)