# Problem: Maximum Number of Zeros - https://codeforces.com/gym/514644/problem/D

import decimal
from typing import Counter
 
n = int(input())
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
 
count = Counter([])
 
temp = 0
zeros = 0
for i in range(n):
 
    if nums1[i] == 0 and nums2[i] == 0:
        temp += 1
    elif nums1[i] == 0:
        continue
 
    elif nums2[i] == 0:
        zeros += 1
 
    else:
        x = decimal.Decimal(nums2[i]) / decimal.Decimal(nums1[i])
 
        count[x] += 1
 
res = temp + zeros
 
for cnt in count.values():
    res = max(res, cnt + temp)
 
print(res)
