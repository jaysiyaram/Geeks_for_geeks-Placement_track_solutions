#code
import sys


def calc_sum(arr):
    max_val = arr[0]
    tmpMax = []
    curr_val = 0
    for value in arr:
        curr_val = max(value, curr_val + value)
        if curr_val > max_val:
            max_val = curr_val
        tmpMax.append(max_val)
    return tmpMax
    

def calc_max_absolute_diff(arr, arr_len):
    import pdb; pdb.set_trace()
    leftMax = calc_sum(arr)
    rightMax = calc_sum(arr[::-1])
    rightMax = rightMax[::-1]
    
    tmpArr = [-1*value for value in arr]
    leftMin = calc_sum(tmpArr)
    rightMin = calc_sum(tmpArr[::-1])
    
    leftMin = [-1*value for value in leftMin]
    rightMin = [-1*value for value in rightMin]
    rightMin = rightMin[::-1]
    
    maxVal = -sys.maxsize - 1
    for i in range(arr_len-1):
        result = max(abs(leftMin[i] - rightMax[i+1]), abs(leftMax[i] - rightMin[i+1]))
        if result > maxVal:
            maxVal = result
            
    return maxVal


test_cases = int(input())
for _ in range(test_cases):
    arr_len = int(input())
    arr = list(map(int, input().split()))
    answer = calc_max_absolute_diff(arr, arr_len)
    print(answer)
