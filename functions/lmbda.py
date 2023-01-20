# name = "royal"
# name = name.upper()
# name = name[::-1]

# print(name)

name = "royal"
rev_upper = lambda x: x.upper()[::-1]
print(rev_upper(name))

no = -5
check = lambda x : x**2 if x>0 else x**3
print(check(no))