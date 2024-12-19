from array import array

numbers = array("i", [5, 3, 1, 4, 2])

numbers.append(6)
numbers.remove(3)
numbers.insert(0, 9)

if numbers:
    print(numbers)
else:
    print("array is empty")

# note: the array is used when we've large amount of data, it can increase the performance instead of using lists