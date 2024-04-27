# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        if s == '':
            return ''
            

        if '1' <= s[0] <= '9':
            j = 0
            while s[j] != '[':
                j += 1

            n = int(s[:j])

            stack = ['[']
            i = j + 1
            while stack:
                if s[i] == '[':
                    stack.append('[')
                if s[i] == ']':
                    stack.pop()
                i += 1
                
            return self.decodeString(s[j + 1:i - 1]) * n + self.decodeString(s[i:])

        i = 0
        while i < len(s) and 'a' <= s[i] <= 'z':
            i += 1
        
        return s[:i] + self.decodeString(s[i:])