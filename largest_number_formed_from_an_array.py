def merge_sort(a_list):
    if len(a_list) > 1:
        mid = len(a_list)//2
        #import pdb; pdb.set_trace()
        left_list = a_list[:mid]
        right_list = a_list[mid:]

        merge_sort(left_list)
        merge_sort(right_list)

        i, j, k = (0,)*3

        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                a_list[k] = left_list[i]
                i += 1
                k += 1
            else:
                a_list[k] = right_list[j]
                j += 1
                k += 1

        while i < len(left_list):
            a_list[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            a_list[k] = right_list[j]
            j += 1
            k += 1

#li = [4, 7, 2, 1, 7, 9]
#merge_sort(li)
#print(li)

test_cases = int(input())
for _ in range(test_cases):
    arr_len = int(input())
    arr = input().split()
    merge_sort(arr)
    print(arr)
    temp = ''
    for i in arr[::-1]:
        temp += i
    print(temp)
