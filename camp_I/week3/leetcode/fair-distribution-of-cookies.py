class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        res = float('inf')
        children = [0] * k

        def backtrack(index):
            nonlocal res
            if index == len(cookies):
                res = min(res, max(children))
                return

            for j in range(k):
                children[j] += cookies[index]
                if children[j] < res:
                    backtrack(index + 1)
                children[j] -= cookies[index]

        backtrack(0)
    
        return res