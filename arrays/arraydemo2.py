import array as array

a = array.array('u', ["a","b","c","d"])
# cnt = a.count(11)
# print("cnt = ", cnt)
# x = a.buffer_info()
# print("x = ", x)

# #a.clear()
# byt = a.tobytes()

# print("byt = ", byt)
uni = a.tounicode()
for i in a:
    print(i, " ", end="")