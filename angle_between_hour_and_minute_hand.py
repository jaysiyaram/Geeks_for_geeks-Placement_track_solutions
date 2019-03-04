test_cases = int(input())
for _ in range(test_cases):
    hour, minute = list(map(float, input().split()))
    if minute in [60, 0]:
        if hour < 6:
            print(int(hour * 30))
        else:
            print(int(360 - hour * 30))
        continue
            
            
    minute_fraction = minute/60
    minute_fraction = minute_fraction * 30
    
    hour_final = hour*30 + minute_fraction
    minute_final = minute * 6
    
    angle = abs(hour_final - minute_final) 
    
    if angle < (360-angle):
        print(int(angle))
    else:
        print(int(360-angle))
