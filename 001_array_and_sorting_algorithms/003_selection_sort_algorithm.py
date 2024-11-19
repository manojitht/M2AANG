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