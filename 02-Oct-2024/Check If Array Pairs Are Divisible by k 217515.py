# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        temp = defaultdict(int)
        for num in arr:
            temp[num % k] += 1

        if temp[0] % 2:
            return False

        for mod in temp:
            if temp[mod] != temp[(k - mod) % k]:
                return False
        
        return True