# The binary search algorithm (it's kind a divide and conquer algorithm)
def binary_search(array, low, high, key):
    mid = (low + high) // 2
    if low <= high:
        if array[mid] == key:
            print(f"The {key} was found in the array index of {mid}.")
        elif key > array[mid]:
            binary_search(array, mid+1, high, key)
        elif array[mid] > key:
            binary_search(array, low, mid-1, key)
    if low > high:
        print(f"Unsuccessful search and {key} not found in array.")

array = [6, 12, 14, 18, 22, 39, 55, 182]
low = 0
high = len(array) - 1
key = 6
binary_search(array, low, high, key)

# The binary search algorithm big O notation is O (logn)
