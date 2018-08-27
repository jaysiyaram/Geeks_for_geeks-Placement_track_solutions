test_cases = int(input())
for _ in range(test_cases):
    arr_len = int(input())
    arr = list(map(int, input().split()))
    
    odd = []
    even = []
    for i in arr:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
            
    odd.sort(reverse=True)
    even.sort()
    
    odd.extend(even)
    for i in odd:
        print(i, end=' ')
        
    print()
