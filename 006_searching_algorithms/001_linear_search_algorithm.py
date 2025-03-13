
nums = [54, 26, 85, 12, 36, 55, 99, 84, 10, 11, 18, 98]

def linear_search(value ,array):
    for i in nums:
        if i == value:
            print(f"Found the {value}.")
            break
        print(f"Stopped with {i}")


linear_search(36, nums)
