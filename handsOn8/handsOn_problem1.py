def partition(arr, p, r):
    x = arr[r]
    i = p - 1  
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1

def quickselect(arr, p, r, i):
    if p == r:
        return arr[p]
    q = partition(arr,p,r)
    k = q-p+1  
    if i == k:  
        return arr[q]
    elif i < k:
        return quickselect(arr,p,q - 1,i)
    else:
        return quickselect(arr,q + 1,r,i-k)



#invoking the algorithm
arr = [5, 9, 3, 2, 18, 14]
print(f"For {arr}")
output = quickselect(arr, 0, len(arr) - 1, 3)
print(f"3rd smallest element is {output}")
output = quickselect(arr, 0, len(arr) - 1, 5)
print(f"5th smallest element is {output}\n")


arr1 = [1,2,3]
print(f"For {arr1}")
output = quickselect(arr1, 0, len(arr1) - 1, 2)
print(f"2nd smallest element is {output}")