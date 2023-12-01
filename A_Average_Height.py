t = int(input())

for _ in range(t):
    n = int(input())
    even_nums = []
    odd_nums = []

    num = 0
    nums = input().split(" ")
    for i in range(len(nums)):
        num = int(nums[i])
        if num % 2 == 0:
            even_nums.append(num)
        else:
            odd_nums.append(num)
    
    output = odd_nums + even_nums
    print(*output)