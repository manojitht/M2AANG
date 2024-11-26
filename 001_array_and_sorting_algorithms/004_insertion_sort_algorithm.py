my_array = [1,1,2]

def removeDuplicates(array):
    dup_set = {}
    for i in range(len(array)):
        dup_set[array[i]] = array[i]
    print(list(dup_set.keys()))



removeDuplicates(my_array)