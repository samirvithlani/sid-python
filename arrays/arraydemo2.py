import array as array

a = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,1,1,1])
cnt = a.count(11)
print("cnt = ", cnt)
x = a.buffer_info()
print("x = ", x)

#a.clear()
byt = a.tobytes()

print("byt = ", byt)
uni = a.tounicode()
for i in a:
    print(i, " ", end="")