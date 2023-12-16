class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        count_s = Counter(s)
        count_t = Counter(t)

        return count_s == count_t