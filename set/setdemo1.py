#list --> duplicate values are allowed   ,,index
#set --> duplicate values are not allowed,,no index  unorder/....

#{} {}

#teams = set()\
username = set()
#username = {"sachin","virat","dhoni","rohit","sachin","virat","dhoni","rohit"}
username.add("sachin")
username.add("virat")
username.add("raj")
username.add("xyz")
print("bfr",username)
#username.remove("virata")
#username.discard("virata")
#print(username.pop())
#username.update(("raj","jay"))
#username.update(["raj","jay"])
#username.update("raj")

#username.copy()
#username = username.union({"raj","jay"})
#x = username.difference({"raj","jay"})
#username.difference_update({"raj","jay"})
#username.intersection_update({"raj","jay"})
print(username.issubset({"raj","sachin","virat"}))
print(username.issuperset({"raj","sachin","virat"}))
print(username.isdisjoint({"raj","sachin","virat"}))
#username.symmetric_difference({"raj","sachin","virat"})

#print(x)
print(username)