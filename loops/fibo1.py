first = 0
second = 1
third =0

print(first)
print(second)

for i in range(1,9):
    third = first + second
    print(third)
    
    first,second = second,third    