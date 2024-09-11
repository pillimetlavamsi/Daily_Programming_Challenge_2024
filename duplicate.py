def to_find_duplicate(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] == arr[j] and i != j:  
                return arr[i] 
    return -1 
arr = [3,1,3,4,2]
duplicate = to_find_duplicate(arr)
print("Duplicate Number is:", duplicate)
