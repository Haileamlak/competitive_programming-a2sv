for _ in range(int(input())):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    prod = 1
    for num in nums:
        prod *= num
    
    if 2023 % prod != 0:
        print("NO")
    else:
        print("YES")
        print(2023//prod, end=" ")
        for i in range(k - 1):
            print(1, end=" ")
        print()