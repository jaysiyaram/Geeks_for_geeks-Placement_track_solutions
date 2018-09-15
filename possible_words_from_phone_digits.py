keymap = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']


def print_words_util(arr, curr_digit, result, arr_len):
    index = 0
    if(curr_digit == arr_len):
        for i in result:
            print(i, end='')
        print(' ', end='')
        return
        
    for i in range(0, len(keymap[arr[curr_digit]])):
        # print('Curr_digit-%s, i-%s'%(curr_digit, i))
        result[curr_digit] = keymap[arr[curr_digit]][i]
        print_words_util(arr, curr_digit+1, result, arr_len)
        


def print_words(arr, arr_len):
    result = [0 for i in range(arr_len)]
    print_words_util(arr, 0, result, arr_len)


test_cases = int(input())
for _ in range(test_cases):
    arr_len = int(input())
    arr = list(map(int, input().split()))
    
    print_words(arr, arr_len)
    print()
    
