# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        class TrieNode:
            def __init__(self):
                self.zero = None
                self.one = None
            
        class Trie:
            def __init__(self):
                self.root = TrieNode()
            
            def insert(self, num):
                curr = self.root
                for i in range(31, -1, -1):
                    if (1 << i) & num:
                        if not curr.one:
                            curr.one = TrieNode()
                        
                        curr = curr.one
                    else:
                        if not curr.zero:
                            curr.zero = TrieNode()
                        
                        curr = curr.zero
        trie = Trie()
        for num in nums:
            trie.insert(num)

        res = 0
        for num in nums:
            curr = trie.root
            temp = 0
            for i in range(31, -1, -1):
                if (1 << i) & num:
                    if curr.zero:
                        temp += (1 << i)
                        curr = curr.zero
                    else:
                        curr = curr.one
                else:
                    if curr.one:
                        temp += (1 << i)
                        curr = curr.one
                    else:
                        curr = curr.zero
                        
            res = max(res, temp)

        return res