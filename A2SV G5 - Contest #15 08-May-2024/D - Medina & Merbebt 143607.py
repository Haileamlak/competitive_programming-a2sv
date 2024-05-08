# Problem: D - Medina & Merbebt - https://codeforces.com/gym/522079/problem/D


for i in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    p = [[0] * 32]

    for num in nums:
        curr = p[-1].copy()
        i = 0
        while num:
            if 1 & num:
                curr[-1 - i] += 1
            num >>= 1
            i += 1
        
        p.append(curr)

    # print(p)
    def _and(l, r):
        res = 0
        for i in range(32):
            if p[r][i] - p[l - 1][i] == r - l + 1:
                res += (1 << (31 - i))
        
        return res
    
    def binary_search(l, k):
        low = l
        high = n
        while low <= high:
            mid = low + (high - low) // 2
            if _and(l, mid) >= k:
                low = mid + 1
            else:
                high = mid - 1
        
        if high < l:
            return -1
        return high

    for i in range(int(input())):
        l, k = map(int, input().split())
        print(binary_search(l, k), end=' ')
    print()