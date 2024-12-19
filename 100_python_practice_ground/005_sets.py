sets = [8, 7, 4, 3, 5]

first = set(sets) # converting into a set with built-in function set()
second = {6, 1, 3, 9}

union = first | second
intersection = first & second
difference = first - second
symmetric_difference = first ^ second

print(union)
print(intersection)
print(difference)
# note: set is a collection with no duplicates in it