my_array = [64, 34, 25, 12, 22, 11, 90, 5]

def selection_sort(array):
    n = len(array)
    for i in range(n - 1):
        min_val = i
        for j in range(i, n):
            if array[j] < array[min_val]:
                min_val = j
        array[i], array[min_val] = array[min_val], array[i]
        print(array)

selection_sort(my_array)

""" the outer loop will run each iteration of the array element """
""" the inner loop will find the minimum value by comparing the first index through the array, 
   and it will swap the position of minimum value to the first index and that first index value to the minimum value's position"""

# Big O complexity is O(N^2), because it has nested loops inside the outer loop