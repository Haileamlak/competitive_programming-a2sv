t = int(input())

for _ in range(t):
    n = int(input())
    up = False
    down = False
    right = False
    left = False
    for i in range(n):
        nums = list(map(int, input().split()))

        if nums[1] > 0:
            up = True
        elif nums[1] < 0:
            down = True
        
        if nums[0] > 0:
            right = True
        elif nums[0] < 0:
            left = True
    
    if up and down and left and right:
        print("NO")
    else:
        print("YES")