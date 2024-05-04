# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def foo(x):
            return ord(x) - ord('a')

        words_bit = []
        for word in words:
            curr_bit = 0
            for letter in word:
                if curr_bit & 1 << foo(letter) == 0:
                    curr_bit += (1 << foo(letter))
            
            words_bit.append(curr_bit)

        res = 0
        for i in range(len(words_bit)):
            for j in range(len(words_bit)):
                if words_bit[i] & words_bit[j] == 0:
                    res = max(res, len(words[i]) * len(words[j]))
        
        return res