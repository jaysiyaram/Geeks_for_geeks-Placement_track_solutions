def win_check(arr, char):
    matches = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]]
    
    for i in range(8):
        if(arr[matches[i][0]] == char and
            arr[matches[i][1]] == char and
            arr[matches[i][2]] == char):
            return True
    return False


def is_valid(arr):
    xcount = arr.count('X') if arr.count('X') else arr.count('x')
    ocount = arr.count('O') if arr.count('O') else arr.count('o')
    
    if(xcount == ocount+1 or xcount == ocount):
        if win_check(arr, 'O'):
            if win_check(arr, 'X'):
                return "Invalid"
            if xcount == ocount:
                return "Valid"
                
        if win_check(arr, 'X') and xcount != ocount+1:
            return "Invalid"
            
        if not win_check(arr, 'O'):
            return "Valid"
        
    return "Invalid"


test_cases = int(input())
for _ in range(test_cases):
    arr = input().split()
    print(is_valid(arr))
