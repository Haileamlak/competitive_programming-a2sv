class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_count = {}

        for ch in s:
            s_count[ch] = s_count.get(ch, 0) + 1

        for ch in t:
            if ch in s_count:
                if s_count[ch] == 1:
                    s_count.pop(ch)
                else:
                    s_count[ch] -= 1
            else:
                return ch
        # else:
        #     return list(s_set)[0]