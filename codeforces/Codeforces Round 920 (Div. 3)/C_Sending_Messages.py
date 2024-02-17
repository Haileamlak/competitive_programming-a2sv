t = int(input())

for _ in range(t):
    n, f, a, b = map(int, input().split())

    nums = list(map(int, input().split()))
    res = 0

    if (nums[0] * a) < b:
        f -= (nums[0] * a)
    else:
        f -= b

    for i in range(n - 1):
        x = (nums[i + 1] - nums[i]) * a 
        if x < b:
            f -= x
        else:
            f -= b
    
    if f > 0:
        print("YES")
    else:
        print("NO")
