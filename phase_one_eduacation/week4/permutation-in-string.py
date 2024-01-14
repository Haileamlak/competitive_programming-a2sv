class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        word = [0 for i in range(26)]
        temp = [0 for i in range(26)]
        for i in range(len(s1)):
            word[ord(s1[i]) - 97] += 1
            temp[ord(s2[i]) - 97] += 1
        
        if word == temp:
            return True
        
        for i in range(len(s1), len(s2)):
            temp[ord(s2[i]) - 97] += 1
            temp[ord(s2[i - len(s1)]) - 97] -= 1

            if word == temp:
                return True
                
        return False