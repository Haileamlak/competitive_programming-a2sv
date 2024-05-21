# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        curr = [ch for ch in s]
        alpha = [i for i in range(len(s)) if s[i].isalpha()]

        result = []
        for permutation in range(1 << len(alpha)):
            for i in range(len(alpha)):
                index = alpha[i]
                if (1 << i) & permutation:
                    curr[index] = curr[index].upper()
                else:
                    curr[index] = curr[index].lower()

            result.append(''.join(curr))
    
        return result