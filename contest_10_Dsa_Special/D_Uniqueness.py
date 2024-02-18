n = int(input())
a = list(map(int, input().split()))

min_segment = float('inf')
left_seen = set()
a.append(0) # appended to handle edge cases (to avoid writing if conditions) 

for left in range(n):

    num = a[left]
    right_seen = set()

    for right in range(n, left - 1, -1):
        if a[right] in left_seen or a[right] in right_seen:
            break

        right_seen.add(a[right])
        min_segment = min(min_segment, right - left)
    
    if num in left_seen:
        break

    left_seen.add(num)
    

print(min_segment)



# n = int(input())
# nums = list(map(int, input().split()))
# res  = 0

# l = 0
# temp = set()
# r = n - 1
# while l < n and nums[l] not in temp:
#     temp.add(nums[l])
#     l += 1

# # a = l

# # temp = set()
# while r >= 0 and nums[r] not in temp:
#     temp.add(nums[r])
#     r -= 1


# res = 0
# if l <= r:
#     res = r - l + 1

# l = 0
# temp = set()
# r = n - 1

# while r >= 0 and nums[r] not in temp:
#     temp.add(nums[r])
#     r -= 1

# # b = r
# while l < n and nums[l] not in temp:
#     temp.add(nums[l])
#     l += 1

# if l <= r:
#     res = min(res, r - l + 1)
    
#     # res  = min(res, max(a, b) - min(a,b) + 1)
# print(res)