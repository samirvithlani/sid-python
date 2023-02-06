subjects =[('English',88,6),('Science',90,5),('Maths',97,9),('Social sciences',82,1)]
print("Original list of tuples:")
print(subjects)
subjects.sort(key=lambda x:x[2])
print("List of tuples after sorting:")
print(subjects)

marks = [[100,"raj"],[90,"ram"],[80,"ravi"],[70,"rakesh"],[60,"rakul"]]
marks.sort(key=lambda x:x[1])
print(marks)