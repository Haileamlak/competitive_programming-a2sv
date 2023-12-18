class Solution:
    def minimizedStringLength(self, s: str) -> int:
        s_arr = []
        index = {}
        for i in range(len(s)):
            if s[i] in index:
                pass
            else:
                s_arr.append(s[i])
                index[s[i]] = i
        
        return len(s_arr)