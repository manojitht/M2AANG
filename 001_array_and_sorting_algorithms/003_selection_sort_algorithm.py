my_array = [64, 34, 25, 12, 22, 11, 90, 5]

def selection_sort(array):
    global min_val
    n = len(array)
    ss_list = []

    for i in range(n - 1):
        for j in range(n - i - 1):
            min_val = array[0]
            if array[j + 1] < min_val:
                min_val = array[j + 1]
        ss_list.append(min_val)

    print(ss_list)
                

selection_sort(my_array)