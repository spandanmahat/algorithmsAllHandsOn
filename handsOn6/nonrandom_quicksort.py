import timeit
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

def quicksort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quicksort(arr, p, q - 1)
        quicksort(arr, q + 1, r)




#average case
random_arr0 = random.sample(range(1, 101),5)
random_arr1 = random.sample(range(1, 101),10)
random_arr2 = random.sample(range(1, 101),15)
print(random_arr0,random_arr1,random_arr2)

random_arr0_time = timeit.timeit('quicksort(random_arr0, 0, len(random_arr0)-1)', setup='from __main__ import quicksort, random_arr0', number=1000)
print(f"quick Sort Time (average case): {random_arr0_time}")
random_arr1_time = timeit.timeit('quicksort(random_arr1, 0, len(random_arr1)-1)', setup='from __main__ import quicksort, random_arr1', number=1000)
print(f"quick Sort Time (average case): {random_arr1_time}")
random_arr2_time = timeit.timeit('quicksort(random_arr2, 0, len(random_arr2)-1)', setup='from __main__ import quicksort, random_arr2', number=1000)
print(f"quick Sort Time (average case): {random_arr2_time}")

average_time = (random_arr0_time + random_arr1_time + random_arr2_time) / 3
print(f"Average QuickSort Time (average case): {average_time}")



#worst case
worstcase_arr0 = list(range(1, 6))
worstcase_arr1 = list(range(20, 31))
worstcase_arr2 = list(range(45, 61))
print(worstcase_arr0,worstcase_arr1,worstcase_arr2)

worstcase_arr0_time = timeit.timeit('quicksort(worstcase_arr0, 0, len(worstcase_arr0)-1)', setup='from __main__ import quicksort, worstcase_arr0', number=1000)
print(f"quick Sort Time (worstcase case): {worstcase_arr0_time}")
worstcase_arr1_time = timeit.timeit('quicksort(worstcase_arr1, 0, len(worstcase_arr1)-1)', setup='from __main__ import quicksort, worstcase_arr1', number=1000)
print(f"quick Sort Time (worstcase case): {worstcase_arr1_time}")
worstcase_arr2_time = timeit.timeit('quicksort(worstcase_arr2, 0, len(worstcase_arr2)-1)', setup='from __main__ import quicksort, worstcase_arr2', number=1000)
print(f"quick Sort Time (worstcase case): {worstcase_arr2_time}")

worstcase_average_time = (worstcase_arr0_time + worstcase_arr1_time + worstcase_arr2_time) / 3
print(f"Average QuickSort Time (worstcase case): {worstcase_average_time}")




#best case
bestcase_arr0 = [1, 5, 2, 4, 3]
bestcase_arr1 = [2, 7, 1, 9, 4, 8, 3, 10, 6, 5]
bestcase_arr2 = [4, 12, 2, 10, 7, 14, 1, 15, 5, 13, 3, 11, 6, 9, 8]
print(bestcase_arr0,bestcase_arr1,bestcase_arr2)

bestcase_arr0_time = timeit.timeit('quicksort(bestcase_arr0, 0, len(bestcase_arr0)-1)', setup='from __main__ import quicksort, bestcase_arr0', number=1000)
print(f"quick Sort Time (bestcase case): {bestcase_arr0_time}")
bestcase_arr1_time = timeit.timeit('quicksort(bestcase_arr1, 0, len(bestcase_arr1)-1)', setup='from __main__ import quicksort, bestcase_arr1', number=1000)
print(f"quick Sort Time (bestcase case): {bestcase_arr1_time}")
bestcase_arr2_time = timeit.timeit('quicksort(bestcase_arr2, 0, len(bestcase_arr2)-1)', setup='from __main__ import quicksort, bestcase_arr2', number=1000)
print(f"quick Sort Time (bestcase case): {bestcase_arr2_time}")

bestcase_average_time = (bestcase_arr0_time + bestcase_arr1_time + bestcase_arr2_time) / 3
print(f"Average QuickSort Time (bestcase case): {bestcase_average_time}")



