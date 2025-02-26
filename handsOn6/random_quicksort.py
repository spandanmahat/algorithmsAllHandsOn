import random

def partition(arr, p, r):
    x = arr[r]
    i = p - 1  
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1

def randomized_partition(arr, p, r):
    i = random.randint(p, r)
    arr[i], arr[r] = arr[r], arr[i]
    return partition(arr, p, r)

def randomized_quicksort(arr, p, r):
    if p < r:
        q = randomized_partition(arr, p, r)
        randomized_quicksort(arr, p, q - 1)
        randomized_quicksort(arr, q + 1, r)


arr = [13,19,9,5,12,8,7,4,21,2,6,11]
randomized_quicksort(arr, 0, len(arr) - 1)
print(arr)
