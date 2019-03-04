#code
def find_longest_pallindrome(inp_str):
    str_len = len(inp_str)
    track_arr = [[0 for x in range(str_len)] for y in range(str_len)]
    max_len = 1
    start_i = 0

    import pdb; pdb.set_trace()

    # Fixing positions in track_arr for single chars
    for i in range(str_len):
        track_arr[i][i] = 1

    # Checking for consecutive value and setting track_arr accordingly
    for i in range(str_len - 1):
        if inp_str[i] == inp_str[i+1]:
            track_arr[i][i+1] = 1
            max_len = 2
            start_i = i

    # Checking for values greater than 2 
    k = 3
    while k < str_len:
        for i in range(str_len-k+1):
            j = i+k-1
            if inp_str[i] == inp_str[j] and track_arr[i+1][j-1]:
                track_arr[i][j] = 1
                if k > max_len:
                    max_len = k
                    start_i = i
        k += 1
    
    return max_len, start_i, k


test_cases = input()
for _ in range(test_cases):
    inp_str = input().strip()
    answer, i, k = find_longest_pallindrome(inp_str)
    print(inp_str[i:i+k-1])
