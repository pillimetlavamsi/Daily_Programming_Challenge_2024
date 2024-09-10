def to_find_missing_number(arr):
    n = len(arr) + 1 
    expected_sum = (n * (n + 1)) // 2   
    received_sum = sum(arr) 
    return expected_sum - received_sum

arr=[1,2,3,4,5,7,8,9]    
missing_no=to_find_missing_number(arr)
print("Missing number is:",missing_no)    
