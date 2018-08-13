test_cases = int(input())
for _ in range(test_cases):
    arr_len = int(input())
    arr = list(map(int, input().split()))
    
    i = 0
    # First we are checking whether the array is ascending or not
    while(i<arr_len-1 and arr[i] <= arr[i+1]):
        i += 1
    
    # if yes then print the highest and the ascending code.
    if i == arr_len-1:
        print(arr[i], 1)
        continue
        
    # Next we check for descending order
    if i==0:
        while(i<arr_len-1 and arr[i] >= arr[i+1]):
            i += 1
        
        # if yes then print the highest and descending code
        if i == arr_len-1:
            print(arr[0], 2)
            continue
            
        # If the code is descending in starting and then the order breaks at certain point
        # it means that pattern is descending rotated
        if arr[0] < arr[i+1]:
            print(arr[i+1], 3)
            continue
        # This is the case where in which pattern is ascending rotated but the break point is the 
        # very start of the string "5 1 2 3 4"
        else:
            print(arr[0], 4)
            continue
            
    # If the code is ascending in starting and then the order breaks at certain point
    # it means that pattern is ascending rotated
    if i<arr_len-1 and arr[0] > arr[i+1]:
        print(arr[i], 4)
        continue
    # This is the case where in which pattern is descending rotated but the break point is the 
    # very start of the string "1 5 4 3 2"
    else:
        print(arr[i], 3)
        continue
