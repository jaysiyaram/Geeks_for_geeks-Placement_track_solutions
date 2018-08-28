# This is another solution for sort in specific order problem
# Making all the odd numbers negative and then sort whole array
# Once sort is done make odd numbers positive.
test_cases = int(input())
for _ in range(test_cases):
    arr_len = int(input())
    arr = list(map(int, input().split()))
    
    for i in range(arr_len):
        if arr[i] & 1:
            arr[i] *= -1
        
    arr.sort()
    
    for i in range(arr_len):
        if arr[i] & 1:
            arr[i] *= -1
            
    print(*arr)
