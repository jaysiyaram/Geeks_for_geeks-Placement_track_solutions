class Description():
    """Given a list of non negative integers, arrange them in such a manner that they form the largest number possible.
        
        The result is going to be very large, hence return the result in the form of a string.
        
        Input:
        
        The first line of input consists number of the test cases. The description of T test cases is as follows:
        
        The first line of each test case contains the size of the array, and the second line has the elements of the array.
        
        
        Output:
        
        In each separate line print the largest number formed by arranging the elements of the array in the form of a string.
        
        
        Constraints:
        
        1 ≤ T ≤ 70
        1 ≤ N ≤ 100
        0 ≤ A[i] ≤ 1000
    """


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
            if compare(left_list[i],right_list[j]):
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

def compare(l_val, r_val):
    val1 = int(l_val + r_val)
    val2 = int(r_val + l_val)
    if val1 > val2:
        return True
    else:
        return False

#li = [4, 7, 2, 1, 7, 9]
#merge_sort(li)
#print(li)

test_cases = int(input())
for _ in range(test_cases):
    arr_len = int(input())
    arr = input().split()
    merge_sort(arr)
    #print(arr)
    temp = ''
    for i in arr:
        temp += i
    print(temp)
