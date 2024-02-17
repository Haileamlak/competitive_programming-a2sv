from collections import Counter
n = int(input())
nums = list(map(int, input().split()))

count = Counter(nums)
nums = sorted(list(count))

rem = count[nums[0]]

res = 0
for i in range(1, len(nums)):
    res += min(rem, count[nums[i]])
    rem = max(rem, count[nums[i]])
    # if count[nums[i]] <= rem:
    #     res += count[nums[i]]
    #     rem =  rem - count[nums[i]]
    
    # else:
    #     res += count[nums[i - 1]]
    #     temp = count[nums[i]] - count[nums[i - 1]]
    #     if temp >= rem:
    #         res += rem
    #         rem = temp - rem
    #     else:
    #         res += temp
    #         rem = rem - temp

print(res)