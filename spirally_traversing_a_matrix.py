class Question:
    """
    Traverse a 4x4 matrix of integers in spiral form.
    
    Input: 
    The first line of input contains an integer T denoting the number of test cases. 
    First four lines of the test case will contain four elements each.
    
    Output:
    Spiral array will be displayed in a single line.
    
    Constraints:
    1 <=T<= 100
    
    Example:
    Input:
    1
    1 2 3 4
    5 6 7 8
    9 10 11 12
    13 14 15 16
    Output:
    1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
    """


test_cases = int(input())
for _ in range(test_cases):
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    arr3 = list(map(int, input().split()))
    arr4 = list(map(int, input().split()))
    m_arr = []
    m_arr.append(arr1)
    m_arr.append(arr2)
    m_arr.append(arr3)
    m_arr.append(arr4)
    
    i, t, l = 0, 0, 0
    d = len(m_arr) - 1
    r = len(m_arr[0]) - 1
    
    while(t<d and l<r):
        while(i<=r):
            print(m_arr[t][i], end=' ')
            i += 1
        t += 1
        i = t
                
        while(i<=d):
            print(m_arr[i][r], end=' ')
            i += 1
        r -= 1
        i = r
                
        while(i>=l):
            print(m_arr[d][i], end=' ')
            i -= 1
        d -= 1
        i = d
                
        while(i>=t):
            print(m_arr[i][l], end=' ')
            i -= 1
        l += 1
        i = l
            
    print()
