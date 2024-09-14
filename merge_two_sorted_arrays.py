def merge_two_sort_arrays(arr1, arr2, m, n):
    merged_array = arr1 + arr2
    merged_array.sort()
    for i in range(m):
        arr1[i] = merged_array[i]
    for j in range(n):
        arr2[j] = merged_array[m + j]
        
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
m = len(arr1)
n = len(arr2)

merge_two_sort_arrays(arr1, arr2, m, n)

print("arr1:", arr1)
print("arr2:", arr2)
