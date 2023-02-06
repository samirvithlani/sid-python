def create_path(path):
    def addfile(filename):
        return path+filename
    return addfile

x = create_path("C:\\Users\\user\\Desktop\\")
abspath = x("test")
print(abspath)


def data(no):
    def square():
        return no**2
    return square

x1 = data(5)
print(x1())