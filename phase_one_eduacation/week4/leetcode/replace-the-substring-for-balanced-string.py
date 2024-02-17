class Solution:
    def balancedString(self, s: str) -> int:
        # n = len(s)
        # k = n // 4
        # count = Counter(s)

        # left = 0
        # res = n 
        # for right in range(n):
        #     count[s[right]] -= 1

        #     while left < right and count['Q'] <= k and count['W'] <= k and count['R'] <= k and count['E'] <= k:
        #         res = min(res, right - left + 1)
        #         count[s[left]] += 1
        #         left += 1
        
        # return res
        count = collections.Counter(s)
        res = n = len(s)
        i = 0
        for j, c in enumerate(s):
            count[c] -= 1
            while i < n and all(n / 4 >= count[c] for c in 'QWER'):
                res = min(res, j - i + 1)
                count[s[i]] += 1
                i += 1
        return res
