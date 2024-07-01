# Problem: Short Encoding of Words - https://leetcode.com/problems/short-encoding-of-words/

class TrieNode:
    def __init__(self):
        self.children = {}
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.res = 0

    def add(self, word):
        curr = self.root
        for i in range(len(word) - 1, -1, -1):
            letter = word[i]
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            
            curr = curr.children[letter]
        
    def solve(self, curr):
        if len(curr.children) == 0:
            return (1, 1)
        
        length = count_of_words = 0
        for child in curr.children.values():
            temp = self.solve(child) 
            length += temp[0]
            count_of_words += temp[1]

        return (length + count_of_words, count_of_words)

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = Trie()
        for word in words:
            trie.add(word)

        return trie.solve(trie.root)[0]
