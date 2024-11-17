my_array = [64, 34, 25, 12, 22, 11, 90, 5]

def bubble_sort(array):
    swapped = True
    arr_len = len(array)

    while swapped:
        swapped = False
        for i in range(arr_len - 1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                swapped = True
    print(f"The sorted bubble sorted array is {array}")

# another way of doing bubble sort is below code
# def bubble_sort(array):
#     n = len(array)
#
#     for i in range(n - 1):
#         for j in range(n - i - 1):
#             swapped = False
#             if array[j] > array[j + 1]:
#                 array[j], array[j+1] = array[j+1], array[j]
#                 swapped = True
#         if not swapped:
#             break
#     print(f"The sorted bubble sorted array is {array}")

bubble_sort(my_array)