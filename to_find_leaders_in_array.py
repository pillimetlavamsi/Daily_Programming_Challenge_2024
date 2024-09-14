def to_find_the_leaders_in_array(arr):
    n=len(arr)
    Leaders=[]
    
    for i in range(n):
        is_leader=True
        for j in range (i+1,n):
            if(arr[i]<=arr[j]):
                is_leader=False
                break
        if(is_leader):
            Leaders.append(arr[i])
    return Leaders

arr=[16,17,4,3,5,2]   
Leaders=to_find_the_leaders_in_array(arr)
print("Leaders are:",Leaders)
    
            
            
        