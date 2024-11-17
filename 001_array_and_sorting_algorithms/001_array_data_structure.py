my_array = [7, 12, 9, 4, 2, 11]

def minimum_value(array):
    min_val = array[0]
    for i in array:
        if i < min_val:
            min_val = i
    print(f"The minimum value in the array is {min_val}.")

minimum_value(my_array)