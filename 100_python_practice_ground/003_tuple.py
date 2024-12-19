# point = 1, 2, "egg", "class"
# print(type(point))

point = (1, 0, "egg", "class") # note: tuples are immutable, but can have different types like (str, int)

if point:
    print(point[1])
else:
    print("tuple is empty")