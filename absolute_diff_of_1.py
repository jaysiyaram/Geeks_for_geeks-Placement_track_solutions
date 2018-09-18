#code
def check_for_scene(i):
    chars = str(i)
    for i, v in enumerate(chars):
        if i < len(chars)-1:
            diff = abs(int(v) - int(chars[i+1]))
            if diff != 1:
                return False
    return True


test_cases = int(input())
for _ in range(test_cases):
    readline = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    
    result = []
    for i in arr:
        if check_for_scene(i) and i/9>1:
            if i < readline[1]:
                result.append(i)
            
    if result:
        for i in result:
            print(i, end=' ')
        print()
    else:
        print(-1)
        
