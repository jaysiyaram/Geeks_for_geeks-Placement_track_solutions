test_cases = int(input())
for _ in range(test_cases):
    arr_len = int(input())
    arr = list(map(str, input().split()))
    
    temp = arr[0]
    #print(temp)
    index = 0
    flag = 0
    value = ''
    
    while True:
        prev = value
        if index < len(temp):
            value += temp[index]
        else:
            break
        #print(temp[index], value)
        for i in arr:
            #print(i, value)
            if i.startswith(value):
                continue
            else:
                flag = 1
                break
        index += 1
        if flag:
            break
        
    if prev:
        print(prev)
    else:
        print(-1)
