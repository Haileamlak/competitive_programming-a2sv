class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        for i in range(1, len(s)):
            temp = s[i]
            j = i
            while j > 0 and temp[-1] < s[j - 1][-1]:
                s[j] = s[j - 1]
                j -= 1
            
            s[j] = temp
        
        for i in range(len(s)):
            s[i] = s[i][:-1]
        
        return ' '.join(s)
