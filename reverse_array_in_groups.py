import math


test_cases = int(input())
for _ in range(test_cases):
    arr_len = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    number_of_iterations = math.ceil(arr_len / k)
    last_slice_value = arr_len % k
    start = 0
    end = k
    temp_arr = []
    for i in range(number_of_iterations):
        if last_slice_value == 0 or i < number_of_iterations - 1:
            temp = arr[start:end]
            temp.reverse()
            temp_arr.extend(temp)
            start = end
            end += k
        else:
            temp = arr[start:]
            temp.reverse()
            temp_arr.extend(temp)
        
    for i in temp_arr:
        print(i, end=' ')
    print()
    
