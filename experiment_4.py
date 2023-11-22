#AIM: WRITE A PROGRAM TO PERFORM SEARCHING ACTIVITY USING LINEAR AND BINARY SEARCH.
#Linear Search

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

# Example of using linear search
my_list = [10, 5, 7, 2, 9, 15]
target_value = 7
result = linear_search(my_list, target_value)

if result != -1:
    print(f"Linear Search: Element {target_value} found at index {result}")
else:
    print(f"Linear Search: Element {target_value} not found")

#Binaey search

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Return the index if the target is found
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Return -1 if the target is not found

# Example of using binary search
sorted_list = [2, 5, 7, 9, 10, 15]
target_value = 7
result = binary_search(sorted_list, target_value)

if result != -1:
    print(f"Binary Search: Element {target_value} found at index {result}")
else:
    print(f"Binary Search: Element {target_value} not found")