dict = {1: "Raj", 2: "Ram", 3: "Parth", 4: "Priya"}
filteteddic = {}
# for i,j in dict.items():
#     if len(j)>3:
#         filteteddic[i] = j



filteteddic = {i :j for i,j in dict.items() if len(j)>3}
print(filteteddic)        