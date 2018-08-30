test_cases = int(input())
for _ in range(test_cases):
    arr_len = int(input())
    arr = list(map(int, input().split()))
    
    temp = sorted(arr)
    # print(temp)
    
    if arr_len & 1:
        index = arr_len//2
    else:
        index = (arr_len-1)//2
        
    arr[index] = temp[0]
    for i in range(1, arr_len):
        if i & 1:
            index = index + i
            # print(i, index, temp[i])
            arr[index] = temp[i]
        else:
            index = index - i
            # print(i, index, temp[i])
            arr[index] = temp[i]
            
    print(*arr)
        
