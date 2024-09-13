# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        def get_bit_representation(word):
            ans = 0
            for letter in word:
                i = ord(letter) - ord('a')
                ans |= (1 << i)

            return ans
        
        res = 0
        allowed_in_bit = get_bit_representation(allowed)
        for word in words:
            word_in_bit = get_bit_representation(word)
            if word_in_bit & allowed_in_bit == word_in_bit:
                res += 1
        
        return res