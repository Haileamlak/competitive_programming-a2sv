class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        def contains(s, t):
            for ch in t:
                if s[ch] < t[ch]:
                    return False

            return True
            
        t_map = Counter(t)
        win_map = defaultdict(int)
        
        left = 0
        res = len(s) + 1
        resStr = ""
        for right in range(len(s)):
            win_map[s[right]] += 1

            while contains(win_map, t_map):
                if right - left + 1 < res:
                    resStr = s[left:right + 1]
                    res = right - left + 1
                
                win_map[s[left]] -= 1
                left += 1
        
        return resStr