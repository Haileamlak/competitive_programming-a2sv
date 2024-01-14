n = int(input())
nums = list(map(int, input().split()))
s, f = map(int, input().split())

k = f - s

win_sum = 0
for i in range(k):
    win_sum += nums[i]

res = win_sum
hour = s

for i in range(n - 1):
    idx = (i + k) % n
    win_sum -= nums[i]  
    win_sum += nums[idx]

    if win_sum == res:
        temp = s - (i + 1)
        if temp <= 0:
            temp += n

        hour = min(hour, temp)

    elif win_sum > res:
        res = win_sum
        temp = s - (i + 1)
        if temp <= 0:
            temp += n

        hour = temp



print( hour)