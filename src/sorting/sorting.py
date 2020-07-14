# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    index_a = 0
    index_b = 0
    for i in range(elements):
            # Make sure that we aren't past the end of either of the two input arrays
        if index_a == len(arrA):
            merged_arr[i] = arrB[index_b]
            index_b += 1
        elif index_b == len(arrB):
            merged_arr[i] = arrA[index_a]
            index_a += 1
        # Set merged array at i to the smaller of the two elements at the current index in either array
        # Increment appropriate index
        elif arrA[index_a] < arrB[index_b]:
            merged_arr[i] = arrA[index_a]
            index_a += 1
        else:
            merged_arr[i] = arrB[index_b]
            index_b += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr
    left = arr[:len(arr)// 2]
    right = arr[len(arr)// 2:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
#def merge_in_place(arr, start, mid, end):
    # Your code here


#def merge_sort_in_place(arr, l, r):
    # Your code here
