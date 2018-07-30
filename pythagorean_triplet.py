class Description:
    """
    Given an array of integers, write a function that returns true if there is a triplet (a, b, c) that satisfies a2 + b2 = c2.
    
    Input:
    The first line contains 'T' denoting the number of testcases. Then follows description of testcases.
    Each case begins with a single positive integer N denoting the size of array.
    The second line contains the N space separated positive integers denoting the elements of array A.
    
    Output:
    For each testcase, print "Yes" or  "No" whtether it is Pythagorean Triplet or not.
    """


test_cases = int(input())
for _ in range(test_cases):
    arr_len = int(input())
    arr = list(map(int, input().split()))
    if arr_len < 2:
        continue
    for i in range(arr_len):
        arr[i] = arr[i] * arr[i]
    flag = 1
    arr.sort()
    for i in range(arr_len-1, 1, -1):
        j = 0
        k = i-1
        while j < k:
            if arr[j] + arr[k] == arr[i]:
                print("Yes")
                flag = 0 
                break
            elif arr[j] + arr[k] < arr[i]:
                j += 1
            else:
                k -= 1
        # Many subsets will be formed if we
        # do not terminate the code here
        # Thus, breaking the loop once we find one set.
        if not flag:
            break
    if flag:
        print("No")

