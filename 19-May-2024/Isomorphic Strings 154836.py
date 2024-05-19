# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        temp = {}

        used = set()
        for ch1, ch2 in zip(s, t):
            if ch1 in temp:
                if temp[ch1] != ch2:
                    return False
                    
            else:
                if ch2 in used:
                    return False

                temp[ch1] = ch2
                used.add(ch2)
        
        return True